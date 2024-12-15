import React, { useState } from 'react';
import Message from './Message';
import { sendMessage } from '../services/apiService';

function ChatInterface() {
  const [messages, setMessages] = useState([
    { text: "Welcome to Sleep Better! I'm Frodo, your personal sleep consultant. How may I assist you today?", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    // Add user message
    const newMessages = [...messages, { text: input, sender: 'user' }];
    setMessages(newMessages);
    setInput('');

    try {
      const response = await sendMessage(input);
      setMessages([...newMessages, { text: response, sender: 'bot' }]);
    } catch (error) {
      setMessages([...newMessages, { text: "Sorry, I'm having trouble processing your request.", sender: 'bot' }]);
    }
  };

  return (
    <div className="chat-interface">
      <div className="messages">
        {messages.map((msg, index) => (
          <Message key={index} text={msg.text} sender={msg.sender} />
        ))}
      </div>
      <div className="input-area">
        <input 
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatInterface;