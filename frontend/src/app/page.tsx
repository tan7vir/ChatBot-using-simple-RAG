import Image from "next/image";
import styles from "./page.module.css";
import LeftSide from "@/components/LeftSide";
import RightSide from "@/components/RightSide";

export default function Home() {
  return (
    <div className={styles.mainpage}> 
      {
        /* Air*/
      }

      <div className={styles.Leftside}>
        <LeftSide />
      </div>

      <div className={styles.RightSide}>
        <RightSide />
      </div>
      
    </div>
  );
}
