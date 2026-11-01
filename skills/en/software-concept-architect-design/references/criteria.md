# Concept qualification

A concept is functionality a user understands and uses for a purpose. State/actions define its
behavior; an operational principle shows a useful result. Check all eight criteria.

| Criterion | Question and example |
| --- | --- |
| User-facing | What behavior does the user experience? API programmers are users too. |
| Semantic | Does it describe meaningful state and behavior? Color or a widget alone is insufficient. |
| Independent | Can it be understood without another concept? Comment targets an item identity without defining Post. |
| Behavioral | What can users do and obtain? A list of object properties is insufficient. |
| Purposive | Does it serve one independently valuable need? A step may belong to a larger concept. |
| End-to-end | Does behavior reach the useful result? Authentication needs verification, not registration alone. |
| Familiar | Can users reuse prior knowledge? Prefer familiar behavior or justified variants; novelty alone is not a defect. |
| Reusable | Can its meaning work elsewhere? Existing reuse does not replace purpose, completeness, or independence. |

| Candidate | Boundary decision |
| --- | --- |
| Class | May implement a concept; its class boundary alone proves nothing. |
| Optional function | Private accounts may be an approval option in Following. |
| User story | Today's attendance entry may be part of Attendance; check the term summary or other useful outcome. |
| Microservice | Deployment does not establish a concept boundary. |

Record evidence and a conclusion for each criterion. Resolve disputed boundaries through actual
scenarios, not file/table counts or implementation form.
