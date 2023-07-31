# problem 01:
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name. If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address. If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com". It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

# Example:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# Solution:

# To solve this problem in Python, we can iterate through each email in the given array and apply the rules for transforming the local name. 

# We can use a set to keep track of unique transformed email addresses, and the size of the set will represent the number of different addresses that actually receive mails.

def numUniqueEmails (emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        unique_emails.add(local + '@' + domain)

    return len(unique_emails)

# Example usage
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
result = numUniqueEmails(emails)
print(result)

# Explanation:

# The code splits each email into the local name and the domain name using the split() method with "@" as the delimiter. Then, it applies the transformations by splitting the local name again using "+" as the delimiter and considering only the first part. It also removes any dots (".") from the local name using the replace() method.

# Finally, it concatenates the transformed local name with the original domain name and adds it to the set of unique email addresses.

# By returning the length of the set of unique email addresses, we get the number of different addresses that actually receive mails.




####### Thanks for Watching #####