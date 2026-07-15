function Message({ message }) {
    const isUser = message.role === "user";

    return (
        <div
            className={`flex mb-6 ${isUser ? "justify-end" : "justify-start"
                }`}
        >
            <div
                className={`max-w-[85%] md:max-w-[70%] rounded-2xl px-4 py-3 shadow-sm
          ${isUser
                        ? "bg-blue-600 text-white"
                        : "bg-white border"
                    }
        `}
            >
                <p className="whitespace-pre-wrap break-words">
                    {message.content}
                </p>
            </div>
        </div>
    );
}

export default Message;