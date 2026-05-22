import re

def is_fake_internship(description):
    """
    A simplified AI agent to detect potential fake internship listings.
    This is a proof-of-concept based on common red flags.
    """
    description = description.lower()
    
    # Red flag 1: Vague job duties or requirements
    vague_keywords = ["general tasks", "various duties", "learn on the job", "flexible role"]
    if any(keyword in description for keyword in vague_keywords):
        return True, "Vague job duties or requirements."

    # Red flag 2: Unrealistic promises or lack of detail about the company
    unrealistic_promises = ["guaranteed job offer", "make millions", "easy money"]
    if any(promise in description for promise in unrealistic_promises):
        return True, "Unrealistic promises."

    # Red flag 3: Requests for personal financial information upfront
    financial_info_requests = ["bank details", "social security number", "credit card"]
    if any(request in description for request in financial_info_requests):
        return True, "Requests for personal financial information upfront."

    # Red flag 4: Poor grammar and spelling (simplified check)
    # A more robust check would involve NLP libraries
    if len(re.findall(r'[a-z]+ [A-Z]', description)) > 5: # Example: detects many instances of lowercase followed by uppercase without a period
        return True, "Poor grammar and spelling detected."

    # Red flag 5: Lack of specific company information or contact details
    # This is harder to check without external data, but we can look for absence of common elements
    if "company name" not in description and "about us" not in description and "contact" not in description:
        return True, "Lack of specific company information."
        
    # If no red flags are found, assume it's likely legitimate (for this simplified model)
    return False, "Potentially legitimate."

if __name__ == "__main__":
    # Example internship descriptions
    real_listing = """
    Software Engineering Intern
    Join our dynamic team at Tech Solutions Inc. We are looking for motivated students to assist with web development projects. Responsibilities include coding, testing, and debugging. Must have basic knowledge of Python and JavaScript. Apply with your resume and cover letter. Visit our careers page for more details.
    """

    fake_listing_vague = """
    Amazing Opportunity Intern
    Do you want to learn and grow? We offer a flexible role where you can explore various duties. Great experience guaranteed. Apply now!
    """
    
    fake_listing_financial = """
    Data Entry Clerk
    Work from home! We need someone to help with data entry. Please provide your bank account details and social security number to get started. Quick payment!
    """

    fake_listing_poor_grammar = """
    Marketing Assistant Position
    we are seeking a talented individual to help with our social media campaigns. you will create content and engage with our audience. experience is a plus. send your CV.
    """

    print("--- Checking Real Listing ---")
    is_fake, reason = is_fake_internship(real_listing)
    print(f"Is Fake: {is_fake}, Reason: {reason}\n")

    print("--- Checking Fake Listing (Vague) ---")
    is_fake, reason = is_fake_internship(fake_listing_vague)
    print(f"Is Fake: {is_fake}, Reason: {reason}\n")

    print("--- Checking Fake Listing (Financial) ---")
    is_fake, reason = is_fake_internship(fake_listing_financial)
    print(f"Is Fake: {is_fake}, Reason: {reason}\n")
    
    print("--- Checking Fake Listing (Poor Grammar) ---")
    is_fake, reason = is_fake_internship(fake_listing_poor_grammar)
    print(f"Is Fake: {is_fake}, Reason: {reason}\n")
