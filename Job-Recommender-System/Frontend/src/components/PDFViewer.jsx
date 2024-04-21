import React from 'react';
import { useFile } from './FileContext';

function PDFViewer() {
    const { fileUrl } = useFile(); // Get the file URL directly from context

    if (!fileUrl) {
        return <div>No PDF selected or URL is invalid.</div>;
    }

    return (
        <div className="pdf-viewer">
            <h4>Resume Uploaded:</h4>
            <embed src={fileUrl} type="application/pdf" style={{ width: '100%', height: '500px' }} />
        </div>
    );
}

export default PDFViewer;
