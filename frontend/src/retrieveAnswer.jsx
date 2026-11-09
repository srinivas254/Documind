import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import {
  MessageCircle,
  FileText,
  Brain,
  Loader2,
  AlertCircle,
  Search,
} from "lucide-react";

const API_URL = import.meta.env.VITE_API_URL;

export function RetrieveAnswer({ source }) {
  const [query, setQuery] = useState("");
  const [sourceName, setSourceName] = useState("");
  const [fileType, setFileType] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleRetrieve = async (e) => {
    e.preventDefault();

    if (!query.trim()) return;

    setLoading(true);
    setError("");
    setAnswer("");

    try {
      const response = await fetch(`${API_URL}/retrieve`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query.trim(),
          source: sourceName.trim() || null,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Retrieval failed");
      }

      setAnswer(data.answer);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="w-full min-w-0 bg-white rounded-2xl sm:rounded-3xl p-4 sm:p-6 lg:p-7 shadow-sm border border-yellow-100">
      {/* Header */}
      <div className="flex items-center gap-3 mb-6">
        <div className="bg-yellow-100 p-3 rounded-xl">
          <MessageCircle className="text-yellow-700" size={21} />
        </div>

        <div>
          <h2 className="text-lg sm:text-xl font-bold text-gray-900">
            Ask DocuMind
          </h2>
          <p className="text-xs sm:text-sm text-gray-500 mt-0.5">
            Get answers from your uploaded documents
          </p>
        </div>
      </div>

      <form onSubmit={handleRetrieve}>
        {/* Document Filters */}
        <div className="mb-5 p-4 bg-yellow-50 border border-yellow-200 rounded-xl">
          <div className="flex items-center gap-2 mb-4">
            <FileText size={18} className="text-yellow-700" />
            <h3 className="text-sm font-bold text-gray-800">Source Filters</h3>
          </div>

          {/* Document Type */}
          <label className="block text-xs sm:text-sm font-semibold text-gray-700 mb-2">
            Document Type
          </label>

          <select
            value={fileType || (source ? source.split(".").pop().toLowerCase() : "")}
            onChange={(e) => setFileType(e.target.value)}
            className="w-full p-3 text-sm rounded-lg border border-gray-200 bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400"
          >
            <option value="">All document types</option>
            <option value="pdf">PDF</option>
            <option value="docx">DOCX</option>
            <option value="txt">TXT</option>
            <option value="md">Markdown (MD)</option>
            <option value="csv">CSV</option>
          </select>

          {/* Source Filename */}
          <label className="block text-xs sm:text-sm font-semibold text-gray-700 mt-4 mb-2">
            Source Filename
          </label>

          <input
            type="text"
            value={sourceName || source || ""}
            onChange={(e) => setSourceName(e.target.value)}
            placeholder="e.g. report.pdf"
            className="w-full p-3 text-sm rounded-lg border border-gray-200 bg-white focus:outline-none focus:ring-2 focus:ring-yellow-400"
          />

          <p className="text-xs text-gray-500 mt-2">
            Leave the filename empty to search all documents matching the
            selected type.
          </p>
        </div>

        {/* Question */}
        <label className="text-xs sm:text-sm font-semibold text-gray-700">
          Your Question
        </label>

        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask anything about your documents..."
          rows={4}
          className="w-full min-w-0 mt-2 p-3 sm:p-4 text-sm sm:text-base rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-yellow-400 resize-none transition"
        />

        {/* Submit */}
        <button
          type="submit"
          disabled={loading || !query.trim()}
          className="w-full mt-4 bg-gray-900 hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed text-white text-sm sm:text-base font-bold py-3.5 px-3 rounded-xl transition flex items-center justify-center gap-2 cursor-pointer"
        >
          {loading ? (
            <>
              <Loader2 size={18} className="animate-spin" />
              Searching knowledge base...
            </>
          ) : (
            <>
              <Search size={18} />
              Retrieve Answer
            </>
          )}
        </button>
      </form>

      {/* Error */}
      {error && (
        <div className="mt-5 p-3 bg-red-50 border border-red-100 rounded-xl flex items-start gap-2">
          <AlertCircle size={17} className="text-red-600 shrink-0 mt-0.5" />
          <p className="text-xs sm:text-sm text-red-600 break-words">{error}</p>
        </div>
      )}

      {/* Answer */}
      {answer && (
        <div className="mt-5 sm:mt-6 bg-yellow-50 border border-yellow-200 rounded-2xl p-4 sm:p-5">
          <div className="flex items-center gap-2 mb-3">
            <Brain size={19} className="text-yellow-700" />
            <h3 className="text-sm sm:text-base font-bold text-gray-900">
              DocuMind's Answer
            </h3>
          </div>

          <div className="text-gray-700 text-sm sm:text-base leading-7 break-words">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{answer}</ReactMarkdown>
          </div>
        </div>
      )}
    </section>
  );
}
