import React from 'react'

import aiLogo from '@/assets/ai.png'
import userLogo from '@/assets/User.png'
import Image from 'next/image'
import styles from '@/styles/LeftSide.module.css'

function LeftSide() {
  return (
    <div className = {styles.leftSide}>
      {
         /* Air */
      }
      <div  className = {styles.heading}> 
        <Image className= {styles.logo} src={aiLogo} alt="AI" width={36} height={36} />
        <h1 className={styles.text1}>Physics ChatBOT</h1>
      </div>

      {
         /* Air */
      }

      <div className = {styles.user}>
        <Image className= {styles.logo} src={userLogo} alt="User" width={36} height={36} />
        <h1 className={styles.text1}>User Name</h1>
      </div>


    </div>
  )
}

export default LeftSide