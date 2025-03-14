document.getElementById('uploadForm').onsubmit = async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const loadingMessage = document.getElementById('loadingMessage');
    const errorMessage = document.getElementById('errorMessage');
    const downloadLink = document.getElementById('downloadLink');
    
    // Reset display
    loadingMessage.style.display = 'block';
    errorMessage.style.display = 'none';
    downloadLink.style.display = 'none';
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(await response.text());
        }
        
        const data = await response.json();
        loadingMessage.style.display = 'none';
        
        // Setup download link
        downloadLink.href = `/download/${data.filename}`;
        downloadLink.style.display = 'inline-block';
        
        // Automatically start download
        window.location.href = `/download/${data.filename}`;
        
    } catch (error) {
        loadingMessage.style.display = 'none';
        errorMessage.textContent = 'Error: ' + error.message;
        errorMessage.style.display = 'block';
        console.error('Error:', error);
    }
};