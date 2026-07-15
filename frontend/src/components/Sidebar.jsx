import { X } from "lucide-react";

function Sidebar({ isOpen, onClose }) {
  return (
    <>
      {isOpen && (
        <div
          onClick={onClose}
          className="fixed inset-0 bg-black/40 z-30 md:hidden"
        />
      )}


      <aside
        className={`
          fixed md:static
          top-16 left-0
          h-[calc(100vh-4rem)]
          w-72
          bg-white
          border-r
          shadow-lg md:shadow-none
          z-40
          transform
          transition-transform
          duration-300
          ease-in-out
          ${
            isOpen
              ? "translate-x-0"
              : "-translate-x-full md:translate-x-0"
          }
        `}
      >
        <div className="flex flex-col h-full p-5">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-semibold">
              Documents
            </h2>


            <button
              onClick={onClose}
              className="md:hidden p-2 rounded-lg hover:bg-gray-100 transition"
            >
              <X size={22} />
            </button>
          </div>
          <div className="flex-1">
            <div className="rounded-lg border border-dashed p-6 text-center text-gray-500">
              No documents uploaded
            </div>
          </div>
        </div>
      </aside>
    </>
  );
}

export default Sidebar;