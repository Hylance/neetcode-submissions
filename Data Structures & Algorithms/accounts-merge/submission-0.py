class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_name = {}
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(email, first_email)
                email_name[email] = name
        group = defaultdict(list)
        for email in parent:
            root = find(email)
            group[root].append(email)
        res = []
        for root, emails in group.items():
            name = email_name[root]
            res.append([name] + sorted(emails))
        return res