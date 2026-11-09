import { Brain } from "lucide-react";
import { UploadDocument } from "./uploadDocuments";
import { RetrieveAnswer } from "./retrieveAnswer";
import { useState } from "react";

export function HomePage() {
    const [selectedSource, setSelectedSource] = useState("");

  return (
    <div className="min-h-screen bg-[#FFFDF5] overflow-x-hidden">
      {/* Navbar */}
      <nav className="bg-white border-b border-yellow-100 px-4 sm:px-6 lg:px-8 py-3 sm:py-4 lg:py-5">
        <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
          <div className="flex items-center gap-2 sm:gap-3 shrink-0">
            <div className="bg-yellow-400 p-2 sm:p-2.5 rounded-xl">
              <Brain size={22} className="text-gray-900 sm:w-6 sm:h-6" />
            </div>

            <h1 className="text-xl sm:text-2xl font-extrabold text-gray-900 tracking-tight">
              Docu<span className="text-yellow-500">Mind</span>
            </h1>
          </div>

          <span className="text-[10px] sm:text-xs md:text-sm font-medium text-gray-500 text-right leading-tight">
            AI-Powered Document
            <span className="hidden sm:inline"> Intelligence</span>
          </span>
        </div>
      </nav>

      {/* Main */}
      <main className="w-full max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero Section */}
        <section className="text-center pt-12 pb-10 sm:pt-16 sm:pb-12 md:pt-20 md:pb-16 lg:pt-24 lg:pb-20">
          <span className="inline-block bg-yellow-100 text-yellow-800 text-[9px] min-[375px]:text-[10px] sm:text-xs font-bold tracking-wider px-3 sm:px-4 py-2 rounded-full mb-5 sm:mb-6">
            YOUR PERSONAL AI KNOWLEDGE ASSISTANT
          </span>

          <h2 className="text-[32px] min-[375px]:text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold text-gray-900 leading-[1.15] tracking-tight">
            Your Documents.
            <br />
            <span className="text-yellow-500">One Intelligent Mind.</span>
          </h2>

          <p className="text-gray-500 text-sm sm:text-base md:text-lg mt-5 sm:mt-6 max-w-xl lg:max-w-2xl mx-auto leading-relaxed px-1">
            Upload your documents, ask questions, and discover insights with
            AI-powered hybrid search and retrieval.
          </p>
        </section>

        {/* Application Components */}
        <section className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6 lg:gap-8 items-start pb-12 sm:pb-16">
          <div className="w-full min-w-0">
           <UploadDocument
        onUploadSuccess={setSelectedSource}
      />
          </div>

          <div className="w-full min-w-0">
            <RetrieveAnswer
        source={selectedSource}
      />
          </div>
        </section>

        {/* Footer */}
        <footer className="text-center border-t border-yellow-100 py-7 sm:py-8">
          <p className="text-xs sm:text-sm text-gray-800">
            Powered by LangChain • Hybrid Retrieval • RAG
          </p>

          <p className="text-[10px] sm:text-xs text-gray-600 mt-2">
            © 2026 DocuMind
          </p>
        </footer>
      </main>
    </div>
  );
}
