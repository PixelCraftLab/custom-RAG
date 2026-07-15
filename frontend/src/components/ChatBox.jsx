import MessageList from "./MessageList";

function ChatBox({ messages }) {
    return (
        <div className="flex-1 overflow-y-auto bg-gray-50">
            <div className="max-w-4xl mx-auto px-4 py-6">
                {messages.length === 0 ? (
                    <div className="h-full flex items-center justify-center mt-24">
                        <div className="text-center">
                            <h2 className="text-3xl md:text-5xl font-bold mb-4">
                                Welcome to Custom RAG
                            </h2>

                            <p className="text-gray-500">
                                Upload a PDF and start chatting with it.
                                OR <br></br>
                                Ask question about the default document, which is a RAG Docs<br></br>
                                <span className="text-blue-600">Ex:'Explain RAG'/'what is rag?'</span>
                            </p>
                        </div>
                    </div>
                ) : (
                    <MessageList messages={messages} />
                )}
            </div>
        </div>
    );
}

export default ChatBox;