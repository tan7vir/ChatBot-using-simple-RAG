import { useState } from 'react';

function DropdownComponent() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen((prev) => !prev);
  };

  return (
    <div className="relative inline-flex">
      <button
        onClick={toggleDropdown}
        className="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-blue-500 text-white shadow-sm hover:bg-blue-400 focus:outline-none"
        aria-haspopup="menu"
        aria-expanded={isOpen}
        aria-label="Dropdown"
      >
        Actions
        <svg
          className={`transition-transform ${isOpen ? 'rotate-180' : ''}`}
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="m6 9 6 6 6-6" />
        </svg>
      </button>

      {isOpen && (
        <div
          className="absolute left-0 mt-2 min-w-60 bg-black text-white shadow-md rounded-lg"
          role="menu"
          aria-orientation="vertical"
          aria-labelledby="dropdown-button"
        >
          <div className="p-1 space-y-0.5">
            <a
              className="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm hover:bg-gray-700 focus:outline-none"
              href="#"
            >
              Newsletter
            </a>
            <a
              className="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm hover:bg-gray-700 focus:outline-none"
              href="#"
            >
              Purchases
            </a>
            <a
              className="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm hover:bg-gray-700 focus:outline-none"
              href="#"
            >
              Downloads
            </a>
            <a
              className="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm hover:bg-gray-700 focus:outline-none"
              href="#"
            >
              Team Account
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

export default DropdownComponent;
