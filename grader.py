from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
score = 0
feedback = []

# Check for h1
if soup.find("h1"):
    score += 2
    feedback.append("✔ h1 tag found")
else:
    feedback.append("✘ h1 tag missing")

# Check for img with src and alt
img = soup.find("img")
if img and img.get("src") and img.get("alt"):
    score += 2
    feedback.append("✔ Image tag with src and alt found")
else:
    feedback.append("✘ Image tag with src and alt not found")

# Check for h2
if soup.find("h2") and "features" in soup.find("h2").text.lower():
    score += 1
    feedback.append("✔ h2 heading for features found")
else:
    feedback.append("✘ h2 heading for features missing or incorrect")

# Check list
ul = soup.find("ul")
if ul and len(ul.find_all("li")) >= 3:
    score += 2
    feedback.append("✔ List of 3 features found")
else:
    feedback.append("✘ List with 3 <li> items not found")

# Check for Buy Now link
link = soup.find("a", href=True)
if link and "buy now" in link.text.lower():
    score += 1
    feedback.append("✔ 'Buy Now' link found")
else:
    feedback.append("✘ 'Buy Now' link not found")

# Output result
print("\n".join(feedback))
print(f"Final Score: {score}/8")
exit(0 if score == 8 else 1)
