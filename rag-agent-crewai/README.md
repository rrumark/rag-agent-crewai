RAG AGENT CREWAI

🔍 Overview

This repository contains a Retrieval-Augmented Generation (RAG) Agent built using CrewAI.
The agent answers user queries by grounding its responses in a document-based knowledge source, rather than relying only on a large language model.

The knowledge base is provided as a PDF document (RAG_MAS.pdf) focused on RAG-based Multi-Agent Systems.

🎯 The main goal of this project is to demonstrate how RAG improves reliability by generating answers strictly based on retrieved document content.

🧠 RAG Pipeline

The agent follows a standard Retrieval-Augmented Generation workflow:

🔎 Retrieve
Relevant sections are retrieved from the PDF knowledge base using semantic search.

🧩 Augment
The retrieved context is combined with the user query.

✍️ Generate
A response is generated using only the retrieved document content, reducing hallucinations.

In short, the agent answers questions only using facts present in the document.

⚙️ Tech Stack

CrewAI – Agent orchestration framework

Groq (ChatGroq) – LLaMA 3.1 8B Instant model

HuggingFace – all-MiniLM-L6-v2 embeddings

RagTool (CrewAI) – PDF-based retrieval tool

ChromaDB – Vector database (CrewAI default)

Python – Core implementation

python-dotenv – Environment variable management

🧑‍💼 Agent Design
SOW RAG Agent

Role: Senior SOW Assistant

Goal: Answer questions related to Statements of Work

Background: Expert in contracts and compliance, focused on document-based fact retrieval

Tools: RAG Tool for PDF retrieval

🔄 Project Workflow

Load the PDF knowledge base (e.g., SOW or RAG documentation)

Initialize the RAG tool with the document source

Configure the RAG agent with role, goal, and tools

Define tasks that query the agent, such as:

What is the waiting period for rehabilitation?

What is the standard timeline for completing a Statement of Work draft?

What review steps are required before final SOW approval?

Execute the task and generate a grounded response

⭐ Why This Project

Demonstrates how to build a RAG agent using CrewAI

Shows integration of Groq-hosted LLaMA models

Uses embedding-based semantic retrieval for document Q&A

Focuses on factual accuracy through document grounding

📌 Key Notes

This is not a chatbot

Responses are grounded in a document knowledge base

Retrieval-Augmented Generation improves reliability

CrewAI coordinates agents, tools, and execution flow