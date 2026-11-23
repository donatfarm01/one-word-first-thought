Build notes — One Word, First Thought

The bounty asks for exactly one word, the first that comes to mind, judged
two at a time by a model that weighs surprise first, then vividness, then a
spark of wit, sound or double meaning, then whether the word feels chosen
rather than generic. The gate allows one to twenty-four characters of UTF-8
text, so the word had to be short as well as strong.

Fase 1, deconstruction. The cliché radar says most of the field will send
safe filler: love, happy, freedom, banana, serendipity, coffee. Those lose
on surprise before anything else is weighed. The well-known rare-word list
favourites are the second trap: petrichor is vivid, but it sits on every
beautiful-words list, so several entrants are likely to send the exact same
bytes, and identical entries share one rate.

Fase 2, three contrasting concepts, scored one to ten on hook, originality,
sponsor fit, and clarity.

Concept A, a sensory rare word, petrichor, the smell of earth after rain.
Hook eight, originality six, sponsor fit seven, clarity nine. Killed by the
duplication risk and by low surprise against a field full of word-list
favourites.

Concept B, a playful onomatopoeic word, boing. Hook seven, originality six,
sponsor fit seven, clarity eight. Fun to hear, but light; it loses on
surprise and it reads as a sound effect rather than a chosen word.

Concept C, a double-meaning ordinary word, leftovers. Hook seven,
originality eight, sponsor fit eight, clarity eight. A solid everyday word
with a second life, but less surprising than the winner.

The winner is borborygmus, the rumbling sound a stomach makes. Hook nine,
originality nine, sponsor fit nine, clarity eight. Nobody guesses it, so it
wins on surprise. Everyone has felt it, so it is vivid. And the word itself
gurgles like the thing it names, which is exactly the spark of sound the
judge's fourth criterion rewards. It is eleven characters, letters only,
well inside the gate.

Fase 3, adversarial judging. Against petrichor it wins on surprise and on
sound. Against a safe word like love it wins on every criterion. Against
another rare word it still holds the sound advantage, because few rare words
sound like their own meaning. The main risk is obscurity: a judge that does
not know the word might score it as odd rather than vivid. That risk is
accepted because the judge is a language model that knows the word, and
because surprise is the first thing weighed after validity.

The program is a small Python script at the repository root. It writes the
word to the output entry file with no trailing newline, after checking the
gate itself: one to twenty-four characters, exactly one word, letters only,
and a read-back check that what was written matches the word. The script
was written in two versions: the first version wrote the word with the
length and single-word checks, and the second version added the
letters-only check and the read-back self-check. Both versions produce the
same eleven bytes, verified across two runs each.

No numeric floor applies to this bounty; it is judged pairwise by a model,
so there is no local benchmark to run. The repository carries an MIT
license with its SPDX identifier line, and a readme with the three live
make.fun badge lines.
