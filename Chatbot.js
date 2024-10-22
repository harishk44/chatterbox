import React, { useState } from 'react';

const Chatbot = () => {
  const [input, setInput] = useState('');
  const [history, setHistory] = useState([]); // State to store the history of Q&A
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    // Store the question to later add it to the history
    const question = input;

    try {
      const res = await fetch('http://localhost:8000/get_response/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          context: "default_context",
          question: input,
        }),
      });

      let data = await res.json();
      let answer = data.response;

      // Check if the question is repeated in the answer and remove it if necessary
      if (answer && answer.toLowerCase().includes(question.toLowerCase())) {
        answer = answer.replace(question, '').trim();
        answer = answer.replace("Question:", '').trim();
        answer = answer.replace("Answer:", '').trim();
      }

      // Update history with the new question and answer
      setHistory((prevHistory) => [
        ...prevHistory,
        { question, answer },
      ]);
    } catch (error) {
      setHistory((prevHistory) => [
        ...prevHistory,
        { question, answer: 'Error fetching the response.' },
      ]);
    } finally {
      setIsLoading(false);
      setInput(''); // Clear input field after submitting the question
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Ask me anything..."
          style={{ width: '300px', padding: '10px' }}
        />
        <button type="submit" style={{ padding: '10px', marginLeft: '10px' }}>
          Ask
        </button>
      </form>

      {isLoading && <p>Loading...</p>}

      {/* Display history of questions and answers */}
      <div style={{ marginTop: '20px' }}>
        {history.length > 0 && (
          <div>
            <h2>History</h2>
            <ul>
              {history.map((item, index) => (
                <li key={index} style={{ marginBottom: '10px' }}>
                  <strong>Q:</strong> {item.question} <br />
                  <strong>A:</strong> {item.answer}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default Chatbot;
