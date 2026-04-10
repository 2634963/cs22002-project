# FessUp Internal Documentation

## API

All API endpoints in this application either accept JSON, return JSON, or both.

They are named in camelCase, despite initially being designed in kebab-case, due to the reliance on the Python module system to expose endpoints,
and the lack of hyphen support in it.

The following API endpoints are implemented:

| Endpoint                  | Accepts JSON                                     | Accepts Cookies | Returns JSON                     | Returns Cookies |
| ------------------------- | ------------------------------------------------ | --------------- | -------------------------------- | --------------- | 
| adminGiveCommentApproval  | commentId, approved                              | authToken       |                                  |                 |
| adminRemoveComment        | commentId, removalReason                         | authToken       |                                  |                 |
| adminRemovePost           | postId, reason                                   | authToken       |                                  |                 |
| adminSetPostApproval      | postId, approved                                 | authToken       |                                  |                 |
| adminViewPostApprovalList |                                                  | authToken       | postId, posterID, title, content |                 |
| createPost                | title, content, extraInfo                        | authToken       |                                  |                 |
| getExtraInformation       | postId                                           | authToken       | extraInfo                        |                 | 
| getUsernameFromUserId     | userId                                           |                 | username                         |                 |
| login                     | username, password                               |                 |                                  | authToken       |
| log                       | *                                                |                 |                                  |                 |
| postComment               | postId, content                                  | authToken       |                                  |                 |
| purchaseExtraInformation  | postId, cardNumber, expireMonth, expireYear, ccv | authToken       |                                  |                 |
| signup                    | username, password                               |                 |                                  |                 |
| viewPostList              |                                                  |                 | postId, posterId, title, content |                 |
| viewPostWithComments      |                                                  |                 | content                          |                 |

[Back](../README.md)