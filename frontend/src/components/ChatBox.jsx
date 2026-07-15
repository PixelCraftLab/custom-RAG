function ChatBox() {
  return (
    <section className="flex-1 h-[calc(100vh-4rem)] overflow-y-auto bg-gray-50">
      <div className="max-w-4xl mx-auto h-full flex items-center justify-center px-4">
        <div className="text-center">
          <h2 className="text-3xl md:text-5xl font-bold mb-4">
            Welcome to Custom RAG
          </h2>

          <p className="text-gray-500 text-base md:text-lg">
            Upload your PDFs and start chatting with them.
          </p>
        </div>
      </div>
    </section>
  );
}

export default ChatBox;