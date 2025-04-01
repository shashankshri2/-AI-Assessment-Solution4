import os
import time
import random
import asyncio
from deep_translator import GoogleTranslator
from twilio.rest import Client

# ✅ Twilio Credentials
TWILIO_SID = "ACb74a8c3483baf2c4119e9c0eff473d22"
TWILIO_AUTH_TOKEN = "3b8f7ba1ea3e9fad5e36d94ef8be5396"
TWILIO_PHONE_NUMBER = "+1 912 319 7187"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"

# ✅ Initialize Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# ✅ Check Twilio Authentication
try:
    client.api.accounts(TWILIO_SID).fetch()
    print("✅ Twilio Authentication Successful!")
except Exception as e:
    print(f"❌ Twilio Authentication Failed: {e}")
    exit()

# ✅ Sample Patients Data (With Language & Preferred Channel)
patients = [
    {"id": 1, "name": "Ravi Kumar", "language": "Tamil", "channel": "SMS", "phone": "+919588623617"},
    {"id": 2, "name": "Ananya Rao", "language": "Telugu", "channel": "WhatsApp", "phone": "+919527920242"},
    {"id": 3, "name": "Joseph Mathew", "language": "Malayalam", "channel": "IVR", "phone": "+919527920243"},
    {"id": 4, "name": "Rahul Sharma", "language": "Hindi", "channel": "SMS", "phone": "+919588623618"},
    {"id": 5, "name": "David Thomas", "language": "English", "channel": "WhatsApp", "phone": "+919527920244"},
]

# ✅ Predefined Multi-Language Messages
messages = {
    "Tamil": "உங்கள் நேரம் உறுதிசெய்யப்பட்டது. தயவுசெய்து வருக!",
    "Telugu": "మీ నియామకం నిర్ధారించబడింది. దయచేసి రండి!",
    "Malayalam": "നിങ്ങളുടെ അപോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി വരൂ!",
    "Hindi": "आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया आएं!",
    "English": "Your appointment is confirmed. Please visit!"
}

# ✅ Message Templates for Different Reminders (A/B Testing Variants)
reminder_templates = {
    "appointment": {
        "A": "Your appointment is confirmed. Please visit on time!",
        "B": "Reminder! Your doctor appointment is confirmed. See you soon!"
    },
    "wait_time": {
        "A": "Your doctor is running late. Expected wait time: 30 mins.",
        "B": "We apologize for the delay. Estimated wait time: 30 mins."
    },
    "prescription": {
        "A": "Reminder: Please take your medication as prescribed.",
        "B": "It's time for your medicine! Don't forget your dosage."
    }
}

# ✅ AI Translation Function
async def translate_message(message, lang):
    """Translate message to patient's preferred language"""
    if lang in messages:
        return messages[lang]  # Use predefined translations
    return GoogleTranslator(source="auto", target=lang.lower()).translate(message)

# ✅ SMS Sending Function
def send_sms(to, message):
    try:
        client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=to)
        print(f"📩 SMS Sent Successfully to {to}")
    except Exception as e:
        print(f"❌ Error sending SMS to {to}: {e}")

# ✅ WhatsApp Sending Function
def send_whatsapp(to, message):
    try:
        client.messages.create(body=message, from_=TWILIO_WHATSAPP_NUMBER, to=f"whatsapp:{to}")
        print(f"💬 WhatsApp Message Sent to {to}")
    except Exception as e:
        print(f"❌ Error sending WhatsApp to {to}: {e}")

# ✅ IVR Call Function
def make_voice_call(to, message):
    try:
        client.calls.create(twiml=f'<Response><Say>{message}</Say></Response>', from_=TWILIO_PHONE_NUMBER, to=to)
        print(f"📞 IVR Call Triggered to {to}")
    except Exception as e:
        print(f"❌ Error making call to {to}: {e}")

# ✅ Send Reminder Messages
async def send_reminders(reminder_type):
    for patient in patients:
        message_variant = random.choice(list(reminder_templates[reminder_type].values()))  # A/B Test
        translated_message = await translate_message(message_variant, patient["language"])  # AI Translation

        print(f"✅ Sending {reminder_type} to {patient['name']} ({patient['channel']}): {translated_message}")

        if patient["channel"] == "SMS":
            send_sms(patient["phone"], translated_message)
        elif patient["channel"] == "WhatsApp":
            send_whatsapp(patient["phone"], translated_message)
        elif patient["channel"] == "IVR":
            make_voice_call(patient["phone"], translated_message)

        time.sleep(2)  # Simulated delay

# ✅ Simulate Confirmation Tracking
def measure_effectiveness():
    confirmed = sum(random.choices([0, 1], k=len(patients)))  # Random confirmations
    confirmation_rate = (confirmed / len(patients)) * 100

    # A/B Test Results
    responses_variant_1 = random.randint(5, 15)
    responses_variant_2 = random.randint(10, 20)

    # Patient Satisfaction Score (Random 1 to 5 scale)
    satisfaction_score = round(random.uniform(2.5, 4.5), 2)

    print(f"✅ Confirmation Rate: {confirmed} / {len(patients)} ({confirmation_rate:.2f}%)")
    print(f"📈 A/B Test Results - Variant 1: {responses_variant_1} responses, Variant 2: {responses_variant_2} responses")
    print(f"📝 Patient Satisfaction Score: {satisfaction_score}/5")

# ✅ Run the System
if __name__ == "__main__":
    print("\n📅 Sending Appointment Confirmations...")
    asyncio.run(send_reminders("appointment"))

    print("\n⏳ Sending Wait Time Updates (Real-Time)...")
    asyncio.run(send_reminders("wait_time"))

    print("\n💊 Sending Prescription Reminders (Recurring)...")
    asyncio.run(send_reminders("prescription"))

    print("\n📊 Generating Effectiveness Report...")
    measure_effectiveness()
