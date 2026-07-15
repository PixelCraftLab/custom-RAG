import { useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";
import MessageInput from "../components/MessageInput";

function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const handleSend = (question) => {
    console.log(question);

  };

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      <Navbar onMenuClick={() => setSidebarOpen(!sidebarOpen)} />

      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
        />

        <main className="flex-1 flex flex-col">
          <ChatBox />

          <MessageInput
            onSend={handleSend}
            loading={false}
          />
        </main>
      </div>
    </div>
  );
}

export default Home;