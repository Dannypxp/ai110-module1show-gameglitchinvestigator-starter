# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked clean and modern, the range is easy to read and the places to input numbers was working
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. I was given a number outside of the range, my number was -35 when the range is 1-100
2. The higher and lower messages pointed me in the wrong direction
3. Changing the difficulty changed the amount of chances but it did not change the range to guess
4. New Game button does not work after running out of attempts
5. Cant submit when starting a new game after winning
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI Suggested that the hints were giving opposite suggestions. It was correct because when the guess was higher than secret, it will still tell you to go higher
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I didnt get any misleading answers thankfully, I was being specific enough for the AI to point to the errors

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
By testing the game on the web browser
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I did both manual and pytest runs to see if the logic and the actual gameplay mechanic was fixed while bug fixing
- Did AI help you design or understand any tests? How?
AI did help by automatically making pytests for the fixes i made to the app, like the hints giving the correct direction and the guess INT being turned into a STR
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Secret will be converted to str every other guess, so the int values for the camparison kept changing
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain reruns as running the entire code on every interaction and session states are used to keep your progression saved from game to game
- What change did you make that finally gave the game a stable secret number?
Removing the if statement which checked if it was an even or odd round

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I will re use is adding the files as context to get better answers and scope on the problem i want solved
- What is one thing you would do differently next time you work with AI on a coding task?
I will make sure to give it proper context rather than just asking single questions to it
- In one or two sentences, describe how this project changed the way you think about AI generated code.
THis project has changed how I think of AI because it made me realize how much power AI really has to generating code that runs smoothly and quickly with just a proper prompt



fix: keep secret as int and use numerical comparison for higher/lower hints