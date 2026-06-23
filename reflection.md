# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 60, secret 30     | Go Lower hint | Go Higher hint Output is incorrect, vice versa error|  none|
|Pressed new game button | New game, new feedback| No feedback from new guesses. History isn't refreshed, history skips first guess... |  none |
|guess of 78 | Attempts left to decrease 1| Attempts left stayed at 7| none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Opus 4.8 within VS code. I used it to debug problems and made a new window every time I wanted to explore a different problem which was helpful for it to stay focused. I asked it to help me understand first what was at hand before making changes.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
      It correctly suggested how to perform a test for check_guess because it returned a tuple, and it decided to correctly
    test for outcome from the tuple rather than comparing the entire tuple to a string. I checked it by verifying the pytest assert successfully ran as it proposed. This was a great catch AI helped me notice and how it accounted for testing.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
      It incorrectly suggested once to add several lines of code to be able to fix a timing/display issue with the history
    shown for debugging purposes. However, it did acknowledge that another option would be to reorder the lines of code.Sometimes it would also suggest refactoring that I couldn't understand even with context, so I had to reject certain refactoring suggestions. For instance, in the parse_guess refactoring it tried to push for one line to represent several lines of code that I found
    necessary for context/ understanding code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
    First, I ran pytests with AI help if applicable before checking the app itself. I then glanced at the logic of the code fixed to verify I'm truly satisfied with it based on what AI communicated to me. I ran streamlit run app.py in the terminal for me to manually check the app was working as expected after a fix. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
        Performed a pytest to verify parse_guess worked as expected when receiving mock input. Utilized standalone functions and assert.
      It helped identify functions worked accordingly after refactoring edits.
  
- Did AI help you design or understand any tests? How?
  AI helped me create pytests for all logic util functions when I requested I wanted to verify their behavior was consistent after
  moving them from app.py for reference. It helped me understand tests by first suggesting why it would be helpful to have them and essentially summarize what they assesed. They were created after every issue/bug was handled immediately to verify they are addressing the problem at hand.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  A streamlit re run is essentially the app reacting immediately to a user's actions to accurately reflect changes if necessary. If we press a submit button, it'd be critical to know if the input was successfully proccessed with a different screen that informs that. That's when a re run occurs. Additionally, session state preserves previously given information so that no meaningful information is lost when we do a different action like keeping track of a score in a guessing game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would say prompting strategy because that really affected how meaningful my results were to make effective changes in the code. It was helpful to use different sessions with the AI for it to stay focused instead of distracted from previous issues. It was great to understand complex/unknown code by AI contextualizing given logic.

- What is one thing you would do differently next time you work with AI on a coding task?
  Probably not add many different things at once in a prompt or be uncertain about what I might do before making code changes. I caught myself twice that I almost accidentally permitted the game logic to overcomplicate instead of truly understanding the potential problem or exploring more solution options. It was best when the problem was specifc instead of two or three trying to be solved at once, but it was good that AI could pin point me in the right direction by differentiating between them. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I was stunned by how AI generated code could be helpful and efficient for testing code or accomplishing niche fixes ONLY if I requested it that way. It cannot create large scale flawless code, but it can certainly tackle smaller problems little by little with great detail, explained to me simultaneously when I didn't know all Python advanced code.
