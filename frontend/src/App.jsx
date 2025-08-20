import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Loader2, ChefHat, MessageSquare, Mail, Star, TrendingUp } from 'lucide-react'
import './App.css'

function App() {
  const [loading, setLoading] = useState(false)
  const [generatedContent, setGeneratedContent] = useState('')
  const [restaurantData, setRestaurantData] = useState({
    name: 'Bella Vista',
    cuisine: 'Italienisch',
    specialDish: 'Pasta Carbonara',
    language: 'german'
  })

  const generateSocialMedia = async () => {
    setLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/ai/generate-social-media', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          restaurant_name: restaurantData.name,
          cuisine_type: restaurantData.cuisine,
          special_dish: restaurantData.specialDish,
          platform: 'facebook',
          occasion: 'daily post',
          language: restaurantData.language
        })
      })
      
      const data = await response.json()
      if (data.success) {
        setGeneratedContent(data.content)
      } else {
        setGeneratedContent('Fehler: ' + data.error)
      }
    } catch (error) {
      setGeneratedContent('Verbindungsfehler: ' + error.message)
    }
    setLoading(false)
  }

  const generateNewsletter = async () => {
    setLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/ai/generate-newsletter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          restaurant_name: restaurantData.name,
          cuisine_type: restaurantData.cuisine,
          events: ['Live-Musik am Freitag', 'Neue Sommerkarte'],
          specials: ['20% Rabatt auf Pasta', 'Gratis Dessert'],
          language: restaurantData.language
        })
      })
      
      const data = await response.json()
      if (data.success) {
        setGeneratedContent(JSON.stringify(data.newsletter, null, 2))
      } else {
        setGeneratedContent('Fehler: ' + data.error)
      }
    } catch (error) {
      setGeneratedContent('Verbindungsfehler: ' + error.message)
    }
    setLoading(false)
  }

  const optimizeMenu = async () => {
    setLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/ai/optimize-menu', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          dish_name: restaurantData.specialDish,
          ingredients: ['Pasta', 'Speck', 'Eier', 'Parmesan', 'Pfeffer'],
          price: '€14.90',
          cuisine_type: restaurantData.cuisine,
          language: restaurantData.language
        })
      })
      
      const data = await response.json()
      if (data.success) {
        setGeneratedContent(data.description)
      } else {
        setGeneratedContent('Fehler: ' + data.error)
      }
    } catch (error) {
      setGeneratedContent('Verbindungsfehler: ' + error.message)
    }
    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 to-red-50 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <ChefHat className="h-10 w-10 text-orange-600" />
            <h1 className="text-4xl font-bold text-gray-900">Restaurant KI-Agent</h1>
          </div>
          <p className="text-lg text-gray-600">Automatisierte Content-Generierung für Ihr Restaurant</p>
          <Badge variant="secondary" className="mt-2">MVP Version 1.0</Badge>
        </div>

        {/* Restaurant Settings */}
        <Card className="mb-8">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <TrendingUp className="h-5 w-5" />
              Restaurant-Einstellungen
            </CardTitle>
            <CardDescription>
              Konfigurieren Sie Ihre Restaurant-Daten für personalisierte Inhalte
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div>
                <Label htmlFor="restaurant-name">Restaurant Name</Label>
                <Input
                  id="restaurant-name"
                  value={restaurantData.name}
                  onChange={(e) => setRestaurantData({...restaurantData, name: e.target.value})}
                  placeholder="Ihr Restaurant Name"
                />
              </div>
              <div>
                <Label htmlFor="cuisine">Küche</Label>
                <Select value={restaurantData.cuisine} onValueChange={(value) => setRestaurantData({...restaurantData, cuisine: value})}>
                  <SelectTrigger>
                    <SelectValue placeholder="Küche wählen" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="Italienisch">Italienisch</SelectItem>
                    <SelectItem value="Deutsch">Deutsch</SelectItem>
                    <SelectItem value="Französisch">Französisch</SelectItem>
                    <SelectItem value="Asiatisch">Asiatisch</SelectItem>
                    <SelectItem value="International">International</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <Label htmlFor="special-dish">Spezialität</Label>
                <Input
                  id="special-dish"
                  value={restaurantData.specialDish}
                  onChange={(e) => setRestaurantData({...restaurantData, specialDish: e.target.value})}
                  placeholder="Ihr Signature Dish"
                />
              </div>
              <div>
                <Label htmlFor="language">Sprache</Label>
                <Select value={restaurantData.language} onValueChange={(value) => setRestaurantData({...restaurantData, language: value})}>
                  <SelectTrigger>
                    <SelectValue placeholder="Sprache wählen" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="german">Deutsch</SelectItem>
                    <SelectItem value="english">English</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Content Generator */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <MessageSquare className="h-5 w-5" />
                KI-Content Generator
              </CardTitle>
              <CardDescription>
                Generieren Sie automatisch Inhalte für Ihr Restaurant
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="social" className="w-full">
                <TabsList className="grid w-full grid-cols-3">
                  <TabsTrigger value="social">Social Media</TabsTrigger>
                  <TabsTrigger value="newsletter">Newsletter</TabsTrigger>
                  <TabsTrigger value="menu">Menü</TabsTrigger>
                </TabsList>
                
                <TabsContent value="social" className="space-y-4">
                  <div>
                    <h3 className="text-lg font-semibold mb-2">Social Media Post</h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Erstellen Sie ansprechende Posts für Facebook, Instagram und Co.
                    </p>
                    <Button 
                      onClick={generateSocialMedia} 
                      disabled={loading}
                      className="w-full"
                    >
                      {loading ? (
                        <>
                          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                          Generiere...
                        </>
                      ) : (
                        'Social Media Post generieren'
                      )}
                    </Button>
                  </div>
                </TabsContent>
                
                <TabsContent value="newsletter" className="space-y-4">
                  <div>
                    <h3 className="text-lg font-semibold mb-2">Newsletter</h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Erstellen Sie personalisierte Newsletter für Ihre Kunden
                    </p>
                    <Button 
                      onClick={generateNewsletter} 
                      disabled={loading}
                      className="w-full"
                    >
                      {loading ? (
                        <>
                          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                          Generiere...
                        </>
                      ) : (
                        <>
                          <Mail className="mr-2 h-4 w-4" />
                          Newsletter generieren
                        </>
                      )}
                    </Button>
                  </div>
                </TabsContent>
                
                <TabsContent value="menu" className="space-y-4">
                  <div>
                    <h3 className="text-lg font-semibold mb-2">Menü-Optimierung</h3>
                    <p className="text-sm text-gray-600 mb-4">
                      Optimieren Sie Ihre Menü-Beschreibungen für mehr Verkäufe
                    </p>
                    <Button 
                      onClick={optimizeMenu} 
                      disabled={loading}
                      className="w-full"
                    >
                      {loading ? (
                        <>
                          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                          Optimiere...
                        </>
                      ) : (
                        'Menü-Beschreibung optimieren'
                      )}
                    </Button>
                  </div>
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>

          {/* Generated Content Display */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Star className="h-5 w-5" />
                Generierter Content
              </CardTitle>
              <CardDescription>
                Ihr KI-generierter Inhalt erscheint hier
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="min-h-[400px]">
                {generatedContent ? (
                  <div className="bg-gray-50 p-4 rounded-lg">
                    <pre className="whitespace-pre-wrap text-sm text-gray-800">
                      {generatedContent}
                    </pre>
                  </div>
                ) : (
                  <div className="flex items-center justify-center h-[400px] text-gray-500">
                    <div className="text-center">
                      <MessageSquare className="h-12 w-12 mx-auto mb-4 opacity-50" />
                      <p>Wählen Sie eine Option und generieren Sie Ihren ersten Content!</p>
                    </div>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Footer */}
        <div className="text-center mt-8 text-gray-500">
          <p>Restaurant KI-Agent MVP • Powered by OpenAI GPT-4.1-mini</p>
        </div>
      </div>
    </div>
  )
}

export default App

