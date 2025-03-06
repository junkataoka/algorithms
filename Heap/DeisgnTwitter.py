"""
esign Twitter
Solved 
Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

Twitter() Initializes the twitter object.
void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
Example 1:

Input:
["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

Output:
[null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
twitter.follow(1, 2);     // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
twitter.unfollow(1, 2);   // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
Constraints:

1 <= userId, followerId, followeeId <= 100
0 <= tweetId <= 1000
"""


from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userid -> list of [count, tweetids]
        self.followMap = defaultdict(set)   # userid -> set of followeeid

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1  # Increment instead of decrement for clearer chronological order
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []  # Changed to maxHeap for most recent first

        # Add self follow only once during initialization or first follow
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            if tweets:  # Check if user has any tweets
                index = len(tweets) - 1
                count, tweetId = tweets[index]
                # Negative count for maxHeap behavior
                maxHeap.append([-count, tweetId, followeeId, index])
        
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index > 0:  # Check if there are more tweets before accessing index-1
                count, tweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # Prevent unfollowing self
            self.followMap[followerId].discard(followeeId)  # Using discard instead of remove

