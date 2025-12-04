import React, { useState} from "react"

export default function Chat(params) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const sendMessage = async() =>{
    if (inputValue === '') return;
    setInputValue('');
    setMessages([...messages, `You: ${inputValue}`]);

    try {
      const response = await fetch('http://localhost:8000/api/chat/message',{
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          user_id: 'test_user'
        })
      })
      const data = await response.json();

      setMessages(prev => [...prev, 'AI: ${data.response}']);
    } catch (error){
      console.log(error)
      setMessages(prev => [...prev, `AI: Error Connection`]);
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