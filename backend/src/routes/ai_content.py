"""
AI Content Generator Routes for Restaurant KI-Agent
Handles social media content, newsletter, and menu optimization
"""

from flask import Blueprint, request, jsonify
from openai import OpenAI
import os
from datetime import datetime
import json

# Create blueprint
ai_content_bp = Blueprint('ai_content', __name__)

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

@ai_content_bp.route('/generate-social-media', methods=['POST'])
def generate_social_media():
    """Generate social media content for restaurants"""
    try:
        data = request.get_json()
        
        # Extract restaurant information
        restaurant_name = data.get('restaurant_name', 'Restaurant')
        cuisine_type = data.get('cuisine_type', 'International')
        special_dish = data.get('special_dish', '')
        occasion = data.get('occasion', 'daily post')
        platform = data.get('platform', 'facebook')
        language = data.get('language', 'german')
        
        # Create prompt based on platform and language
        if language.lower() == 'german':
            prompt = f"""
            Erstelle einen ansprechenden Social Media Post für {restaurant_name}, ein {cuisine_type} Restaurant.
            
            Details:
            - Plattform: {platform}
            - Anlass: {occasion}
            - Besonderes Gericht: {special_dish}
            
            Der Post soll:
            - Appetitlich und einladend sein
            - Lokale SEO-Keywords enthalten
            - Call-to-Action haben
            - Emojis verwenden
            - Maximal 280 Zeichen für Twitter, 500 für Facebook/Instagram
            
            Erstelle nur den Text, keine Hashtags separat.
            """
        else:
            prompt = f"""
            Create an engaging social media post for {restaurant_name}, a {cuisine_type} restaurant.
            
            Details:
            - Platform: {platform}
            - Occasion: {occasion}
            - Special dish: {special_dish}
            
            The post should:
            - Be appetizing and inviting
            - Include local SEO keywords
            - Have a call-to-action
            - Use emojis
            - Max 280 chars for Twitter, 500 for Facebook/Instagram
            
            Create only the text, no separate hashtags.
            """
        
        # Generate content using OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Restaurant-Marketing und Social Media Content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        generated_content = response.choices[0].message.content.strip()
        
        return jsonify({
            'success': True,
            'content': generated_content,
            'platform': platform,
            'restaurant': restaurant_name,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_content_bp.route('/generate-newsletter', methods=['POST'])
def generate_newsletter():
    """Generate newsletter content for restaurants"""
    try:
        data = request.get_json()
        
        restaurant_name = data.get('restaurant_name', 'Restaurant')
        cuisine_type = data.get('cuisine_type', 'International')
        events = data.get('events', [])
        specials = data.get('specials', [])
        language = data.get('language', 'german')
        
        if language.lower() == 'german':
            prompt = f"""
            Erstelle einen Newsletter für {restaurant_name}, ein {cuisine_type} Restaurant.
            
            Inhalte:
            - Events: {', '.join(events) if events else 'Keine besonderen Events'}
            - Specials: {', '.join(specials) if specials else 'Keine besonderen Angebote'}
            
            Der Newsletter soll:
            - Persönlich und warm sein
            - Betreffzeile enthalten
            - 3-4 Abschnitte haben
            - Call-to-Action für Reservierung
            - Maximal 800 Wörter
            
            Format: JSON mit 'subject' und 'content' Feldern.
            """
        else:
            prompt = f"""
            Create a newsletter for {restaurant_name}, a {cuisine_type} restaurant.
            
            Content:
            - Events: {', '.join(events) if events else 'No special events'}
            - Specials: {', '.join(specials) if specials else 'No special offers'}
            
            The newsletter should:
            - Be personal and warm
            - Include subject line
            - Have 3-4 sections
            - Call-to-action for reservations
            - Max 800 words
            
            Format: JSON with 'subject' and 'content' fields.
            """
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Restaurant-Newsletter und E-Mail-Marketing."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        generated_content = response.choices[0].message.content.strip()
        
        # Try to parse as JSON, fallback to plain text
        try:
            newsletter_data = json.loads(generated_content)
        except:
            newsletter_data = {
                'subject': f'Newsletter von {restaurant_name}',
                'content': generated_content
            }
        
        return jsonify({
            'success': True,
            'newsletter': newsletter_data,
            'restaurant': restaurant_name,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_content_bp.route('/optimize-menu', methods=['POST'])
def optimize_menu():
    """Generate optimized menu descriptions"""
    try:
        data = request.get_json()
        
        dish_name = data.get('dish_name', '')
        ingredients = data.get('ingredients', [])
        price = data.get('price', '')
        cuisine_type = data.get('cuisine_type', 'International')
        language = data.get('language', 'german')
        
        if language.lower() == 'german':
            prompt = f"""
            Erstelle eine appetitliche Menü-Beschreibung für:
            
            Gericht: {dish_name}
            Zutaten: {', '.join(ingredients) if ingredients else 'Nicht angegeben'}
            Preis: {price}
            Küche: {cuisine_type}
            
            Die Beschreibung soll:
            - Appetitlich und verlockend sein
            - Zutaten hervorheben
            - Zubereitungsart erwähnen
            - Allergen-Hinweise enthalten (falls relevant)
            - Maximal 150 Wörter
            - Verkaufsfördernd wirken
            """
        else:
            prompt = f"""
            Create an appetizing menu description for:
            
            Dish: {dish_name}
            Ingredients: {', '.join(ingredients) if ingredients else 'Not specified'}
            Price: {price}
            Cuisine: {cuisine_type}
            
            The description should:
            - Be appetizing and enticing
            - Highlight ingredients
            - Mention preparation method
            - Include allergen notes (if relevant)
            - Max 150 words
            - Be sales-promoting
            """
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Menü-Beschreibungen und Food-Marketing."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        generated_description = response.choices[0].message.content.strip()
        
        return jsonify({
            'success': True,
            'dish_name': dish_name,
            'description': generated_description,
            'price': price,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_content_bp.route('/generate-review-response', methods=['POST'])
def generate_review_response():
    """Generate responses to customer reviews"""
    try:
        data = request.get_json()
        
        review_text = data.get('review_text', '')
        rating = data.get('rating', 5)
        restaurant_name = data.get('restaurant_name', 'Restaurant')
        language = data.get('language', 'german')
        
        if language.lower() == 'german':
            prompt = f"""
            Erstelle eine professionelle Antwort auf diese Kundenbewertung für {restaurant_name}:
            
            Bewertung: {rating}/5 Sterne
            Text: "{review_text}"
            
            Die Antwort soll:
            - Höflich und professionell sein
            - Dankbarkeit zeigen
            - Bei negativen Bewertungen Verbesserung anbieten
            - Bei positiven Bewertungen Freude ausdrücken
            - Maximal 200 Wörter
            - Einladung für zukünftige Besuche
            """
        else:
            prompt = f"""
            Create a professional response to this customer review for {restaurant_name}:
            
            Rating: {rating}/5 stars
            Text: "{review_text}"
            
            The response should:
            - Be polite and professional
            - Show gratitude
            - Offer improvement for negative reviews
            - Express joy for positive reviews
            - Max 200 words
            - Invite for future visits
            """
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Du bist ein Experte für Kundenservice und Review-Management."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        generated_response = response.choices[0].message.content.strip()
        
        return jsonify({
            'success': True,
            'original_review': review_text,
            'rating': rating,
            'response': generated_response,
            'restaurant': restaurant_name,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@ai_content_bp.route('/test-connection', methods=['GET'])
def test_connection():
    """Test OpenAI API connection"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": "Sage 'Hallo' auf Deutsch."}
            ],
            max_tokens=10
        )
        
        return jsonify({
            'success': True,
            'message': 'OpenAI API connection successful',
            'test_response': response.choices[0].message.content.strip()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

