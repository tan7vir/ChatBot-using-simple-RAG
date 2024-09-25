"use client";

import React, { useState } from 'react';
import styles from '@/styles/RightSide.module.css';
import aiLogo from '@/assets/AI.png'
import user from '@/assets/User.png'
import Image from 'next/image';
import DropdownComponent from './DropdownComponent';
import { HashLoader } from 'react-spinners';

function RightSide() {

  // Hooks
  const [message, setMessage] = useState('')
  const [allmessages, setAllMessages] = useState<any[]>([])
  const [isSent, setIsSent] = useState(true)

  const sendMessage = async () => {

    const url = `http://127.0.0.1:5000/api/generate`;

    const messagesToSend = [
      {
        role: "user",
        prompt: message
      }
    ];

    // Indicate that the message has been sent
    setIsSent(false);

    // Send request to backend
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: messagesToSend[0].prompt }),
      });

      const resjson = await res.json();

      // Extract the response message from backend
      const responseMessage = resjson?.response || 'No response text available';
      const responseSources = resjson?.sources || 'No sources available';

      // Combine old and new messages into the message array
      let newAllMessages = [
        ...allmessages,
        {
          role: "user",
          parts: [{ text: message }],
        },
        {
          role: "model",
          parts: [{ text: responseMessage }],
        }
      ];


      // Update state with new message list
      setAllMessages(newAllMessages);
      setIsSent(true);  // Indicate message sending is done
      setMessage('');   // Clear the input field

    } catch (error) {
      console.error('Error:', error);
      setIsSent(true);  // Still update the status in case of error
    }
  } 

  // for Drop Down menue 
  const menuItems = [
    {
      key: 'gemma:2b',
      shortcut: '⌘G2B',
      description: 'Medium level model',
      label: 'Gemma 2b',
      icon: <img src="https://img.icons8.com/?size=100&id=26256&format=png&color=000000" alt="Add Note" />
    },
    {
      key: 'llama2:latest',
      shortcut: '⌘L7B',
      description: 'Large language model',
      label: 'Llama 2',
      icon: <img src="https://img.icons8.com/?size=100&id=15783&format=png&color=000000" alt="llama" />
      
    },
    {
      key: 'nomic-embed-text:latest',
      shortcut: '⌘N170M',
      description: 'Small language model',
      label: 'Nomic-Embed-Text',
      icon: <img src="https://img.icons8.com/?size=100&id=64794&format=png&color=000000" alt="nomic" />
    }
  ];


  return (
    <div className={styles.rightSection}>

      <div className={styles.rightin}>
        <div className={styles.chatgptversion}>

          <DropdownComponent  />

          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>

        </div>

        {
          allmessages.length > 0 ?
            <div className={styles.messages}>
              {allmessages.map((msg, index) => (
                <div key={index} className={styles.message}>
                  <Image src={msg.role === 'user' ? user : aiLogo} width={50} height={50} alt="" />
                  <div className={styles.details}>
                    <h2>{msg.role === 'user' ? 'You' : 'Physics Bot'}</h2>
                    <p>{msg.parts[0].text}</p>
                  </div>
                </div>
              ))}
            </div>
            :
            <div className={styles.nochat}>
              <div className={styles.s1}>
                {/* <Image src={chatgptlogo} alt="chatgpt" height={70} width={70} /> */}
                <h1>How can I help you today?</h1>
              </div>
            </div>
        }

        <div className={styles.bottomsection}>
          <div className={styles.messagebar}>
            <input type='text' placeholder='Message Physics Bot...'
              onChange={(e) => setMessage(e.target.value)}
              value={message}
            />

            {
              isSent ?
                <svg
                  onClick={sendMessage}
                  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 10.5 12 3m0 0 7.5 7.5M12 3v18" />
                </svg>
                :
                <HashLoader color="#36d7b7" size={30} />
            }

          </div>

        </div>
      </div>
    </div>
  )
}

export default RightSide

{/* <div className={styles.rightSide}>

<div className={styles.chatbox}>

  <p> Physcis chatBOT </p>
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="size-6">
    <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
  </svg>

  <div className={styles.noChat}>

    <div className={styles.section1}>
        <Image src={aiLogo} alt="AI Logo" width={100} height={100} />
        <h1> Welcome to the Physics ChatBOT </h1>
    </div>   
  </div>

  <div className={styles.bottomSide}>
    <div className={styles.messageSide}>
      <input type="text" placeholder="Type a message" value={message} onChange={(e) => setMessage(e.target.value)} />

      <svg onClick={sendMessage} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
      </svg>

    
    </div>
  </div>
</div>
</div> */}