import React from 'react';

function formatChatbotMessage(content) {
  // First split by any newline characters to separate distinct blocks of text
  const blocks = content.split('\n');
  // Map through each block of text to process further
  return blocks.map((block, index) => {
    // Now split each block by the numbered point pattern
    const points = block.split(/(?=\d\. )/).filter(point => point.trim() !== '');
    // Return a div for each block that contains paragraphs for each point
    return (
      <div key={index}>
        {points.map((point, subIndex) => (
          <p key={subIndex} style={{ marginBottom: '10px' }}>
            {point.trim()}
          </p>
        ))}
      </div>
    );
  });
}


function Message({ sender, content, timestamp }) {

  const formattedContent = sender === 'chatbot' ? formatChatbotMessage(content) : content;
  return (
    <div className={`message ${sender}`}>
      <p>{formattedContent}</p>
      {timestamp && <div className="timestamp">{timestamp}</div>}
    </div>
  );
}

export default Message;
