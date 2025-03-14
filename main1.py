import cv2
import os
import numpy as np
from utils import read_video, save_video
from trackers import Tracker
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner

def process_video(input_path, output_path):
    try:
        # Get the directory where the script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define paths relative to the script location
        model_path = os.path.join(base_dir, 'models', 'best.pt')
        track_stubs_path = os.path.join(base_dir, 'stubs', 'track_stubs_test.pkl')
        camera_stubs_path = os.path.join(base_dir, 'stubs', 'camera_movement_stub_test.pkl')

        # Read video
        video_frames = read_video(input_path)
        if not video_frames or len(video_frames) == 0:
            raise ValueError("Failed to read video or video is empty")

        # Initialize tracker
        tracker = Tracker(model_path)
        tracks = tracker.get_object_tracks(
            video_frames,
            read_from_stub=True,
            stub_path=track_stubs_path
        )
        tracker.add_position_to_tracks(tracks)
        # Camera movement estimator
        camera_movement_estimator = CameraMovementEstimator(video_frames[0])
        camera_movement_per_frame = camera_movement_estimator.get_camera_movement(
            video_frames,
            read_from_stub=True,
            stub_path=camera_stubs_path
        )
        camera_movement_estimator.add_adjust_positions_to_tracks(tracks,camera_movement_per_frame)

        # View Transformer
        view_transformer = ViewTransformer()
        view_transformer.add_transformed_position_to_tracks(tracks)

        # Interpolate Ball positions
        tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])

        # Speed and distance estimator
        speed_and_distance_estimator = SpeedAndDistance_Estimator()
        speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

        # Assign player teams
        team_assigner = TeamAssigner()
        team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

        for frame_num, player_track in enumerate(tracks['players']):
            for player_id, track in player_track.items():
                team = team_assigner.get_player_team(
                    video_frames[frame_num],
                    track['bbox'],
                    player_id
                )
                tracks['players'][frame_num][player_id]['team'] = team
                tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

        # Assign ball acquisition
        player_assigner = PlayerBallAssigner()
        team_ball_control = []
        
        for frame_num, player_track in enumerate(tracks['players']):
            ball_bbox = tracks['ball'][frame_num][1]['bbox']
            assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

            if assigned_player != -1:
                tracks['players'][frame_num][assigned_player]['has_ball'] = True
                team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
            else:
                # Handle first frame case
                if not team_ball_control:
                    team_ball_control.append(None)
                else:
                    team_ball_control.append(team_ball_control[-1])
                    
        team_ball_control = np.array(team_ball_control)

        # Draw output
        output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

        # Draw camera movement
        output_video_frames = camera_movement_estimator.draw_camera_movement(
            output_video_frames,
            camera_movement_per_frame
        )
        ## Draw Speed and Distance
        speed_and_distance_estimator.draw_speed_and_distance(output_video_frames,tracks)

        # Save video
        save_video(output_video_frames, output_path)
        
        

    except Exception as e:
        print(f"Error processing video: {str(e)}")
        raise