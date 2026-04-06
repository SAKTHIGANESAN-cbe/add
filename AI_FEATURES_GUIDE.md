# 🤖 AI Features Setup Guide

This document explains the three AI features that have been added to your Plastic Waste Management System.

---

## ✨ The Three AI Features

### 1. **AI Waste Image Classifier** (Image Recognition)
Upload a photo of plastic waste and AI automatically identifies:
- The **type** of plastic (Bags, Bottles, Containers, Packaging, Films, etc.)
- Estimated **weight** in kilograms
- **Confidence level** of the classification

**Where to use**: On the "Add Waste Entry" page, click "Upload Image" and let AI fill in waste type and weight.

---

### 2. **Eco-Impact Calculator with AI Recommendations**
Shows environmental metrics for your collection activities:
- **Plastic Saved**: kg diverted from landfills
- **CO₂ Prevented**: Equivalent greenhouse gas prevented
- **Water Saved**: Liters of production water saved
- **Trees Preserved**: Equivalent trees saved
- **Oil Saved**: Liters of crude oil equivalent
- **Landfill Time Delayed**: Years of decomposition time avoided

Plus **AI-Generated Recommendations** based on your collection patterns!

**Where to see it**: On the Dashboard below the statistics cards.

---

### 3. **AI Chatbot Assistant**
An intelligent chatbot that answers questions about:
- How to properly recycle plastic
- Environmental impact of plastic waste
- Tips for reducing plastic consumption
- Best practices for waste collection

**Where to use**: Click the "💬 Chat with AI Assistant" button at the bottom-right of the Dashboard.

---

## 🔧 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Create a new API key
4. Copy the key (save it securely!)

### Step 3: Configure API Key
#### Option A: Using .env file (Recommended)
1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
2. Open `.env` and replace with your actual API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```
3. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

#### Option B: Set Environment Variable (Windows)
```bash
setx OPENAI_API_KEY "sk-your-actual-key-here"
```
Then restart your terminal.

### Step 4: Run the Application
```bash
python app.py
```

---

## 📸 Using the AI Image Classifier

1. Go to **"Add New Waste Entry"** page
2. In the **"🤖 AI Waste Classifier"** section:
   - Click **"📸 Choose Image"** to select a photo
   - Click **"🔍 Classify with AI"** button
3. AI will analyze the image and suggest:
   - Waste type
   - Estimated weight
   - Confidence percentage
4. Click **"✓ Use These Values"** to auto-fill the form
5. Adjust manually if needed and save

**Supported formats**: PNG, JPG, JPEG, GIF (Max 16MB)

---

## 📊 Understanding Eco-Impact Metrics

The dashboard shows how much environmental impact your collection has:

| Metric | Meaning |
|--------|---------|
| **Plastic Saved (kg)** | Amount of plastic diverted from landfills |
| **CO₂ Prevented (kg)** | Equivalent greenhouse gases avoided (based on 850g CO₂ per kg plastic) |
| **Water Saved (L)** | Water saved from not manufacturing new plastic (2.5L per kg) |
| **Trees Preserved** | Equivalent trees saved (0.1 trees per kg of plastic) |
| **Oil Saved (L)** | Crude oil equivalent saved (1.5L per kg) |
| **Landfill Years Delayed** | How many years of decomposition time delayed |

---

## 💬 Using the Chatbot

1. Click **"💬 Chat with AI Assistant"** button (bottom-right of Dashboard)
2. Type your question, e.g.:
   - "How do I recycle plastic bags?"
   - "What's the environmental impact of plastic?"
   - "How can I reduce plastic consumption?"
3. The AI assistant will provide helpful advice
4. Close the chat by clicking the **"✕"** button

**Note**: Conversation history is kept for context, allowing multi-turn conversations.

---

## ⚙️ Configuration Details

### API Models Used
- **Image Classification**: `gpt-4-vision-preview` (requires Vision API access)
- **Recommendations & Chat**: `gpt-3.5-turbo` (faster and cheaper)

### Database Schema
Your existing database doesn't need changes. All AI features work with the current schema.

### File Upload
- Uploads are saved temporarily in `static/uploads/`
- Files are automatically deleted after classification
- Max file size: 16MB

---

## 🛠️ Troubleshooting

### "OpenAI API key not found"
- **Solution**: Ensure your `.env` file is in the same directory as `app.py`
- Check that `OPENAI_API_KEY` is correctly set
- Restart the Flask app after setting the key

### "Image classification failed"
- Ensure the image is clear and shows the plastic waste clearly
- Try with a different image format (JPG, PNG)
- Check your API quota on OpenAI dashboard
- Verify your API key has Vision API access

### "Chatbot not responding"
- Check your OpenAI API quota
- Ensure you have sufficient API credits
- Check internet connection
- Try a simpler question first

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install openai
```

---

## 💡 Tips & Best Practices

### For Image Classification:
- **Best**: Clear, direct photo of plastic waste
- **Good**: Multiple angles, good lighting
- **Avoid**: Blurry images, dark photos, cluttered backgrounds
- The AI will give confidence levels - use manual entry for low confidence results

### For Eco-Impact:
- More data = better recommendations
- Add entries regularly for accurate patterns
- Share your impact with friends to encourage participation

### For Chatbot:
- Ask specific questions for better answers
- Provide context for complex topics
- Use it to learn recycling best practices
- Share helpful advice with others

---

## 🔐 Security Notes

⚠️ **IMPORTANT**:
- **Never** share your OpenAI API key publicly
- **Never** commit `.env` file to Git - it's already in `.gitignore`
- Keep your API key in a safe location
- Monitor your API usage to avoid unexpected charges

---

## 📈 Future Enhancements

Potential features to add:
- [ ] Email notifications for environmental milestone achievements
- [ ] Community leaderboard for waste collection
- [ ] Advanced analytics with trend predictions
- [ ] Integration with recycling centers locator
- [ ] Mobile app version
- [ ] Multi-language support for chatbot

---

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your OpenAI API key is valid
3. Check OpenAI documentation: https://platform.openai.com/docs
4. Review error messages in the Flask app console

---

## 📚 References

- OpenAI API Documentation: https://platform.openai.com/docs/api-reference
- Flask Documentation: https://flask.palletsprojects.com/
- Werkzeug File Upload: https://werkzeug.palletsprojects.com/uploads/

**Last Updated**: April 2026
