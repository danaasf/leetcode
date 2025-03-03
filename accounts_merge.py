# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails_map representing emails_map of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails_map in sorted order. The accounts themselves can be returned in any order.

from typing import List
# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails_map representing emails_map of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails_map in sorted order. The accounts themselves can be returned in any order.

from typing import List



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        my_map = {}
        emails_map= {}
        visited_account= [False] * len(accounts)

        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in emails_map:
                    emails_map[email]=[]
                emails_map[email].append(i) 
            

        print(emails_map)

        def dfs(i,emails):
            if visited_account[i]:
                return 
            
            visited_account[i]=True
            for email in accounts[i][1:]:
                emails.add(email)
                for neighbor in emails_map[email]:
                    dfs(neighbor,emails)

        for i,account in enumerate(accounts):
            if not visited_account[i]:  
                name = account[0]
                emails = set() 
                dfs(i, emails)
                res.append([name] + sorted(emails))

        return res






# sol = Solution()
# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# sol.accountsMerge(accounts)


sol = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(sol.accountsMerge(accounts))