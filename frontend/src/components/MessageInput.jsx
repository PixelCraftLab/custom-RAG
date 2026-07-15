import { useState } from "react";
import { SendHorizontal } from "lucide-react";

function MessageInput({ onSend, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    const text = question.trim();

    if (!text || loading) return;

    onSend(text);
    setQuestion("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="border-t bg-white p-4">
      <div className="max-w-4xl mx-auto flex items-end gap-3">
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a question about your documents..."
          rows={1}
          disabled={loading}
          className="flex-1 resize-none rounded-xl border p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button
          onClick={handleSubmit}
          disabled={loading || !question.trim()}
          className="h-12 w-12 rounded-xl bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition"
        >
          <SendHorizontal size={20} />
        </button>
      </div>
    </div>
  );
}

export default MessageInput;