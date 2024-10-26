Turing Machine Project - Skyscrapers Game

In this project, I used metaprogramming concepts to create a Turing Machine capable of checking whether an input represents a valid solution for a Skyscrapers-type puzzle. The solution is verified across rows, columns, and visibility, using Python scripts to generate necessary code where the complexity would have been too high for manual implementation.

skyscrapers_lines.tms This Turing Machine checks the puzzle rows, ensuring there are no repeated digits. It operates simply: each element in a row is read and checked against the remaining elements until the end of the row. If duplicate digits are found, the machine will return "NO." If all rows meet the rule, it proceeds to the next stage.

skyscrapers_columns.tm Although it seems similar to row checking, column implementation was significantly more challenging. Here, the machine uses states and bits to track the existence of each number in a column. Each state represents a set of bits indicating the presence of numbers from 1 to 4, allowing precise checking by column. Due to the large number of possible states, I used a Python script to generate all combinations and transitions. Essentially, the script creates every possible transition between states and input values, thus saving a substantial amount of work.

At the end of a column, if the resulting state contains a bit string of 1.1.1.1, the column is valid. Otherwise, the machine returns "NO."

skyscrapers_visibility.tms The Turing Machine for checking building visibility is based on a similar concept to column checking but includes additional rules. Depending on the maximum height encountered and the required number of visible buildings, the transitions are specifically constructed to determine the next state. These checks are symmetric and applicable from left to right and vice versa.

If, at the end, the resulting state does not meet the visibility requirements, the machine returns "NO." Otherwise, it proceeds to the next check.

skyscrapers_final.tms The final Turing Machine combines all the above checks in one final step. Success states (YES) from the columns and rows were connected with the initial states of the following machines so that verification proceeds smoothly. After each check, the machine's head is reset to the beginning of the input for the next stage.

Conclusion By using metaprogramming concepts and automated code generation, this project demonstrates an efficient method of creating a complex Turing Machine capable of validating solutions for a Skyscrapers puzzle through a structured sequence of checks.
