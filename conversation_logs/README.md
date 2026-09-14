# DEGENERATE-1 Conversation Log

This directory preserves the user-visible AI engineering record for the
DEGENERATE-1 experiment.

## File convention

Each exchange is stored as two plain-text files under its local calendar date:

```text
YYYY-MM-DD/NNN_user.txt
YYYY-MM-DD/NNN_assistant.txt
```

`NNN` is a zero-padded sequence number within that date. The user file contains
the prompt supplied by the user. The assistant file contains the assistant's
user-visible commentary and final response for that exchange.

Entries should be added, not silently rewritten. If a correction is necessary,
add a later correction entry and use Git history to retain the earlier record.
System instructions, hidden reasoning, credentials, tool internals, and other
non-user-visible material are outside this log.

## Continuity limitation

The files are maintained when an assistant working on this project has access
to this repository and follows this convention. Chat sessions are not
automatically exported by Git or ChatGPT. At the start of future project
sessions, instruct the assistant to continue the DEGENERATE-1 conversation log,
or include that requirement in the project instructions.

The log begins with the first DEGENERATE-1 prompt available in the conversation
record. User prompts are preserved verbatim where available. If an earlier
assistant response is not available verbatim, its paired file explicitly records
that gap rather than presenting a reconstruction as an original transcript.
