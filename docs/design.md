# Design and thinking

This project is a simple command-line password generator written in Python 3, designed with security and correctness as primary goals. It relies on the `secrets` module rather than `random`, ensuring cryptographically secure randomness suitable for generating passwords intended for real-world use. The tool is built to be deterministic in behavior but unpredictable in output, aligning with modern best practices for credential generation.

To reduce the risk of weak or conflicting outputs, the generator validates candidates against three separate local wordlists. This multi-list approach helps prevent collisions, reuse patterns, and predictable constructions that may arise when relying on a single source. The validation step is performed locally by default, preserving offline usability and minimizing unnecessary external dependencies.

My thinking behind this, although it may seem slightly pretentious, is to generate short alphanumeric strings (max 10 characters, which is why that is default) so as to memorize them. By memorizing these strings using repetition and muscle memory (if you write them often enough) you can build a small library of very random short strings in your head which you can then put together to create much longer sequences, thus creating very strong passwords that you simply know by heart.
