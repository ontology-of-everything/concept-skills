# Qualification Criteria

A concept is both a mental construct required to use an app effectively and a coherent unit of
functionality, and they are the same thing. Dynamic behavior defines it. The three parts are the
name, the purpose, and the operational principle: say what it is for and how to use it. A restaurant
reservation's purpose is to ensure a table will be available; the operational principle is to
contact the restaurant, pick a time in advance, and turn up then.

Every concept satisfies the eight criteria below. The second table separates other constructs.

## Decision basis

| Criterion | Decision basis |
| --- | --- |
| User facing | Make a concept from behavior the user experiences. A hidden structure stays implementation support. When designing an API, the programmer is the user. |
| Semantic | A concept is abstract, semantic structure, both static and dynamic. Widgets, color schemes, and UI skins are not concepts. |
| Independent | It can be understood and used without another concept. A comment: pick an artifact, write the thoughts, and they appear with it. The artifact may be a post, a reply, or another comment, and the definition includes none of them. If use requires another concept, it is not independent. |
| Behavioral | Behavior is usually simple. Leave more complex behavior in the interaction among concepts. Upvoting: people upvote items, and the most upvoted rise to the top. A classification such as pond (small, still, a body of water) is not a concept. |
| Purposive | The purpose must be intelligible and bring real value by itself. A role inside a larger concept is not its own concept. A social security number exists so the government can associate pensions with individuals. Obtaining the number is only a role in that concept. |
| End-to-end | Functionality must reach the behavior that fulfills the purpose. User authentication that registers an account must also authenticate. If the OP only says "this action updates state this way," add the fulfilling behavior. |
| Familiar | Users should be able to start without a manual. New concepts are allowed; novelty comes even more from a new combination or a small adjustment of old concepts. Post, friend/follow, upvote, reply, comment, and hashtag are nearly the same across social apps. Better image support and a post-length limit are variants. |
| Reusable | Check purposive, end-to-end, and independent first. Existing reuse does not replace those three, and lack of reuse does not refute them. A meeting identifier lets parties join without each participant being called. Zoom introduced it; Google Meet and Microsoft Teams copied it. |

| Construct | Decision basis |
| --- | --- |
| Class | Usually not user-facing, and rarely independent. Do not make one a concept. |
| Feature | "Accounts can be made private" is an optional approval on the follower concept. Do not make it a separate concept. |
| User story | "Record which students are present today" brings no value by itself. The concept is attendance: daily entry, end-of-term summaries, and perhaps repeated-absence warnings. One story is not an implementation increment. |
| Microservice | A service boundary is not a concept boundary. |
