import {
  Upload,
  FileText,
  Loader2,
  CheckCircle,
  AlertCircle,
  X,
} from "lucide-react";

import { useState } from "react";
const API_URL = import.meta.env.VITE_API_URL;

export function UploadDocument({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a document first.");
      return;
    }

    setLoading(true);
    setError("");
    setMessage("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed");
      }
      
      onUploadSuccess(file.name);
      setMessage(data.message);
      setFile(null);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="w-full min-w-0 bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-6 lg:p-7 shadow-sm border border-yellow-100">
      {/* Header */}
      <div className="flex items-center gap-3 mb-5 sm:mb-6">
        <div className="bg-yellow-100 p-2.5 sm:p-3 rounded-xl shrink-0">
          <Upload className="text-yellow-700" size={21} />
        </div>

        <div className="min-w-0">
          <h2 className="text-lg sm:text-xl font-bold text-gray-900">
            Upload Document
          </h2>

          <p className="text-xs sm:text-sm text-gray-500 mt-0.5">
            Add documents to your knowledge base
          </p>
        </div>
      </div>

      {/* File Upload Area */}
      <label className="flex flex-col items-center justify-center text-center border-2 border-dashed border-yellow-300 rounded-2xl px-3 py-8 sm:py-10 cursor-pointer hover:bg-yellow-50 active:bg-yellow-100 transition">
        <FileText size={36} className="text-yellow-500 mb-3 sm:w-11 sm:h-11" />

        <p className="text-sm sm:text-base font-semibold text-gray-700 break-all">
          {file ? file.name : "Choose a document"}
        </p>

        <p className="text-xs sm:text-sm text-gray-400 mt-2">
          PDF, DOCX, TXT, CSV, MD
        </p>

        <p className="text-[10px] sm:text-xs text-gray-400 mt-1">
          Click to browse files
        </p>

        <input
          type="file"
          accept=".pdf,.docx,.txt,.csv,.md"
          className="hidden"
          onChange={(e) => {
            setFile(e.target.files[0]);
            setError("");
            setMessage("");
          }}
        />
      </label>

      {/* Selected File */}
      {file && (
        <div className="flex items-center gap-3 mt-4 bg-yellow-50 border border-yellow-100 p-3 rounded-xl min-w-0">
          <FileText size={19} className="text-yellow-700 shrink-0" />

          <span className="text-xs sm:text-sm text-gray-700 flex-1 min-w-0 break-all">
            {file.name}
          </span>

          <button
            type="button"
            onClick={() => setFile(null)}
            className="text-gray-500 hover:text-red-500 transition shrink-0 p-1"
            aria-label="Remove selected file"
          >
            <X size={18} />
          </button>
        </div>
      )}

      {/* Upload Button */}
      <button
        type="button"
        onClick={handleUpload}
        disabled={loading || !file}
        className="w-full mt-4 sm:mt-5 bg-yellow-400 hover:bg-yellow-500 active:scale-[0.99] disabled:opacity-50 disabled:cursor-not-allowed text-gray-900 text-sm sm:text-base font-bold py-3 sm:py-3.5 px-3 rounded-xl transition flex items-center justify-center gap-2 cursor-pointer"
      >
        {loading ? (
          <>
            <Loader2 size={18} className="animate-spin shrink-0" />
            <span>Processing document...</span>
          </>
        ) : (
          <>
            <Upload size={18} className="shrink-0" />
            <span>Upload Document</span>
          </>
        )}
      </button>

      {/* Success Message */}
      {message && (
        <div className="mt-5 p-3 bg-green-50 border border-green-100 rounded-xl flex items-start gap-2 min-w-0">
          <CheckCircle size={17} className="text-green-600 shrink-0 mt-0.5" />

          <p className="text-xs sm:text-sm text-green-700 break-words">
            {message}
          </p>
        </div>
      )}

      {/* Error Message */}
      {error && (
        <div className="mt-5 p-3 bg-red-50 border border-red-100 rounded-xl flex items-start gap-2 min-w-0">
          <AlertCircle size={17} className="text-red-600 shrink-0 mt-0.5" />

          <p className="text-xs sm:text-sm text-red-600 break-words">{error}</p>
        </div>
      )}
    </section>
  );
}
