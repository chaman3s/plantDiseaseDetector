"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [error, setError] = useState<string>("");
  const [result, setResult] = useState<number | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setError("");
    setResult(null);

    const selectedFile = e.target.files?.[0];

    if (!selectedFile) {
      setError("Please select an image.");
      return;
    }

    if (!selectedFile.type.startsWith("image/")) {
      setError("Only image files are allowed.");
      return;
    }

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleRemoveImage = () => {
    setFile(null);
    setPreview(null);
    setResult(null);
    setError("");
  };

  const handleUpload = async () => {
    if (!file) {
      setError("No file selected.");
      return;
    }

    try {
      setError("");
      setLoading(true);
      setResult(null);

      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("API error");

      const data = await res.json();
      setResult(data.result);

    } catch (err) {
      setError("Server error. Make sure API is running.");
    } finally {
      setLoading(false);
    }
  };

  const getLabel = (score: number) => {
    if (score > 0.8) return "Leaf 🌿";
    if (score > 0.5) return "Maybe Leaf 🤔";
    return "Not a Leaf ❌";
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-green-200 p-4">

      <div className="w-full max-w-md bg-white rounded-xl shadow-2xl p-6 space-y-5">

        {/* Title */}
        <h1 className="text-2xl font-bold text-center text-green-800">
          🌿 Leaf Detector
        </h1>

        {/* File Input */}
        <div>
          <label className="block text-base font-semibold text-gray-800 mb-2">
            Upload Image
          </label>

          <input
            type="file"
            onChange={handleFileChange}
            className="w-full border-2 border-gray-400 rounded-lg px-3 py-2 bg-white text-black focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>

        {/* Preview with X button */}
        {preview && (
          <div className="relative w-fit mx-auto">
            <img
              src={preview}
              className="w-40 h-40 object-cover rounded-lg border-2 border-gray-400"
            />

            {/* ❌ Remove Button */}
            <button
              onClick={handleRemoveImage}
              className="absolute -top-2 -right-2 bg-red-600 text-white w-7 h-7 rounded-full flex items-center justify-center text-sm font-bold shadow hover:bg-red-700"
            >
              ×
            </button>
          </div>
        )}

        {/* Error */}
        {error && (
          <p className="text-red-600 text-center font-semibold">{error}</p>
        )}

        {/* Button */}
        <button
          onClick={handleUpload}
          disabled={loading}
          className={`w-full py-3 rounded-lg font-bold text-lg transition 
          ${loading 
            ? "bg-gray-400 text-white" 
            : "bg-green-700 hover:bg-green-800 text-white shadow-lg"}`}
        >
          {loading ? "Processing..." : "Predict"}
        </button>

        {/* Result */}
        {result !== null && (
          <div className="bg-gray-200 p-4 rounded-lg text-center border-2 border-gray-300">
            <p className="text-lg font-bold text-black">
              {getLabel(result)}
            </p>
            <p className="text-gray-800">
              Confidence: <b>{(result * 100).toFixed(2)}%</b>
            </p>
          </div>
        )}

      </div>
    </div>
  );
}