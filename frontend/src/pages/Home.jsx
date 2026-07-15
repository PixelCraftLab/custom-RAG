import { useState, useEffect } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";
import MessageInput from "../components/MessageInput";

import {
  sendMessage,
  getDocuments,
  uploadPDF,
  deleteDocument,
} from "../api/ragApi";

function Home() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [documents, setDocuments] = useState([]);

  const loadDocuments = async () => {
    try {
      const response = await getDocuments();
      setDocuments(response.documents);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadDocuments();
  }, []);


  const handleUpload = async (file) => {
    try {
      await uploadPDF(file);
      await loadDocuments();
    } catch (error) {
      console.error(error);
      alert(error.response?.data?.detail || "Upload failed");
    }
  };


  const handleDelete = async (filename) => {
    try {
      await deleteDocument(filename);
      await loadDocuments();
    } catch (error) {
      console.error(error);
      alert(error.response?.data?.detail || "Delete failed");
    }
  };

  const handleSend = async (question) => {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question,
      },
    ]);

    setLoading(true);

    try {
      const response = await sendMessage(question);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.answer,
          sources: response.sources,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      <Navbar
        onMenuClick={() => setSidebarOpen(!sidebarOpen)}
      />

      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
          documents={documents}
          onUpload={handleUpload}
          onDelete={handleDelete}
        />

        <main className="flex-1 flex flex-col">
          <ChatBox messages={messages} />

          <MessageInput
            onSend={handleSend}
            loading={loading}
          />
        </main>
      </div>
    </div>
  );
}

export default Home;