import React, { useState} from "react"

export default function Chat(params) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const sendMessage = async() =>{
    if (inputValue === '') return;
    const userMessage = inputValue;
    setInputValue('');
    setMessages([...messages, `You: ${userMessage}`]);

    setIsLoading(true);
    try {
      const response = await fetch(`${API_URL}/api/chat/message`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage,
          user_id: 'test_user'
        })
      })
      const data = await response.json();

      setMessages(prev => [...prev, `AI: ${data.response}`]);
    } catch (error){
      setMessages(prev => [...prev, 'AI: Error Connection']);
    } finally {
      setIsLoading(false); // Конец загрузки (выполнится в любом случае)
    }
  };
  const handleKeyPress = (e) => {
    if (e.key === "Enter"){
      sendMessage();
    }
  }

  return(
    <div>
      <h1>AI</h1>
      <div>
        {messages.map((msg, index) =>(
          <div key={index}>{msg}</div>
        ))}
      </div>
      {isLoading && (
        <div><div>AI is typting...</div></div>
      )}
      <div>
        <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={handleKeyPress}
        placeholder="Input message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};