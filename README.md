<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>
<body>
  <h1>LangChain LCEL Basics</h1>

  <p>
    This is a very small learning project built to understand the basics of
    <strong>LangChain</strong>, <strong>chaining</strong>, and
    <strong>LCEL</strong>.
  </p>

  <p>The goal of the project is simple:</p>
  <ul>
    <li>take a user question</li>
    <li>place it into a prompt template</li>
    <li>send that prompt to a chat model</li>
    <li>print the model’s answer</li>
  </ul>

  <p>
    This project is intentionally small so the focus stays on the core ideas.
  </p>

  <hr />

  <h2>What this project teaches</h2>

  <p>
    This project demonstrates three important LangChain concepts:
  </p>

  <h3>1. Prompt Template</h3>
  <p>
    A <strong>prompt template</strong> is a reusable prompt with variables
    inside it.
  </p>
  <p>In this project, the variable is:</p>
  <pre><code>{question}</code></pre>
  <p>
    That means we can reuse the same prompt structure with different questions.
  </p>

  <h3>2. Chat Model</h3>
  <p>
    A <strong>chat model</strong> is the LangChain object that sends the prompt
    to an LLM and receives the response.
  </p>
  <p>In this project we use:</p>
  <pre><code>ChatOpenAI(model="gpt-4.1-mini")</code></pre>
  <p>This creates the model object that LangChain will call.</p>

  <h3>3. LCEL Chain</h3>
  <p>
    <strong>LCEL</strong> stands for <strong>LangChain Expression Language</strong>.
  </p>
  <p>
    It allows us to connect components together using the <code>|</code> operator.
  </p>
  <p>In this project:</p>
  <pre><code>chain = prompt | model</code></pre>
  <p>This means:</p>
  <ul>
    <li>first, build the prompt</li>
    <li>then, send it to the model</li>
  </ul>
  <p>
    So the output of the prompt step becomes the input of the model step.
  </p>

  <hr />

  <h2>Project flow</h2>
  <pre><code>Input Dictionary
      |
      v
ChatPromptTemplate
      |
      v
Formatted Prompt
      |
      v
ChatOpenAI
      |
      v
AIMessage
      |
      v
response.content</code></pre>

  <hr />

  <h2>Code</h2>
  <pre><code>from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Answer the following question in one short paragraph:\n\nQuestion: {question}"
)

model = ChatOpenAI(model="gpt-4.1-mini")

chain = prompt | model

response = chain.invoke({"question": "What is LangChain?"})

print(response.content)</code></pre>

  <hr />

  <h2>Line-by-line explanation</h2>

  <h3><code>from dotenv import load_dotenv</code></h3>
  <p>
    Imports the function that loads environment variables from a
    <code>.env</code> file.
  </p>

  <h3><code>from langchain_core.prompts import ChatPromptTemplate</code></h3>
  <p>Imports LangChain’s prompt template class.</p>

  <h3><code>from langchain_openai import ChatOpenAI</code></h3>
  <p>Imports the OpenAI chat model wrapper for LangChain.</p>

  <h3><code>load_dotenv()</code></h3>
  <p>
    Loads environment variables from the <code>.env</code> file, including the API key.
  </p>

  <h3><code>prompt = ChatPromptTemplate.from_template(...)</code></h3>
  <p>Creates a reusable prompt template.</p>
  <p>The template contains this variable:</p>
  <pre><code>{question}</code></pre>
  <p>
    When the chain runs, LangChain replaces that variable with a real value.
  </p>

  <h3><code>model = ChatOpenAI(model="gpt-4.1-mini")</code></h3>
  <p>Creates the chat model object.</p>
  <p>
    This does not run the model yet. It only prepares the model so it can be used
    in the chain.
  </p>

  <h3><code>chain = prompt | model</code></h3>
  <p>Builds the LangChain chain using LCEL.</p>
  <p>This is the most important part of the project.</p>
  <p>It means:</p>
  <ul>
    <li>take the prompt template output</li>
    <li>pass it into the model</li>
  </ul>

  <h3><code>response = chain.invoke({"question": "What is LangChain?"})</code></h3>
  <p>Runs the chain one time.</p>
  <p>
    The dictionary provides the value for <code>{question}</code>.
  </p>
  <p>LangChain then:</p>
  <ol>
    <li>fills the template</li>
    <li>sends the prompt to the model</li>
    <li>returns the model response</li>
  </ol>

  <h3><code>print(response.content)</code></h3>
  <p>Prints only the text of the model’s answer.</p>
  <p>
    The response itself is usually an <code>AIMessage</code> object, and
    <code>.content</code> extracts the text.
  </p>

  <hr />

  <h2>Why this project is useful</h2>
  <p>
    This tiny project helps build the foundation for larger LangChain applications.
  </p>
  <p>It teaches the basic pattern used in many LangChain systems:</p>
  <ul>
    <li>input</li>
    <li>prompt</li>
    <li>model</li>
    <li>output</li>
  </ul>

  <p>
    Once this is understood, it becomes easier to learn more advanced topics such as:
  </p>
  <ul>
    <li>output parsers</li>
    <li>prompt chaining</li>
    <li>retrievers</li>
    <li>RAG</li>
    <li>agents</li>
    <li>structured output</li>
  </ul>

  <hr />

  <h2>Requirements</h2>
  <p>Install the dependencies with:</p>
  <pre><code>pip install langchain langchain-openai python-dotenv</code></pre>

  <hr />

  <h2>Environment variables</h2>
  <p>Create a <code>.env</code> file in the project root:</p>
  <pre><code>OPENAI_API_KEY=your_api_key_here</code></pre>

  <hr />

  <h2>How to run</h2>
  <pre><code>python main.py</code></pre>

  <hr />

  <h2>Key LangChain ideas from this project</h2>
  <ul>
    <li><strong>PromptTemplate</strong> = reusable prompt with variables</li>
    <li><strong>Chat Model</strong> = object that sends prompts to the LLM</li>
    <li><strong>Chain</strong> = components connected together</li>
    <li><strong>LCEL</strong> = pipe-style syntax using <code>|</code></li>
    <li><strong>invoke()</strong> = runs the chain once</li>
    <li><strong>response.content</strong> = extracts the text from the AI response</li>
  </ul>

  <hr />

  <h2>One-sentence summary</h2>
  <p>
    This project shows how to build a basic LangChain LCEL pipeline that takes a question,
    inserts it into a prompt template, sends it to a chat model, and prints the answer.
  </p>
</body>
</html>
