"""Projects shown on the Projects page.

Each project renders as a sliding card and as a case-study panel that opens
when the card is clicked. Images live in media/.
"""

# The tools used across all projects. Edit here to change every project at once,
# or give a single project its own list instead of STACK.
STACK = ['Python', 'Django', 'JavaScript', 'HTML', 'Dataset', 'SQLite']

# Shown as "Context" in each case study.
CONTEXT = 'School Project'

PROJECTS = [
    {
        'slug': 'fiscal',
        'number': '01',
        'title': 'Fiscal Management System',
        'category': 'Document management system',
        'tagline': 'Organizing barangay fiscal records so every file is easy to find.',
        'image': 'fiscal.jpg',
        'image_alt': 'Fiscal Management System project',
        'context': CONTEXT,
        'summary': (
            'A document management system developed to organize and manage fiscal records '
            'in Brgy. Larrazabal, Naval, Biliran, including complaints and case documents.'
        ),
        'challenge': (
            'Complaints and case documents are hard to keep track of when they are stored '
            'and handled by hand, so finding the right file takes time.'
        ),
        'solution': (
            'A web system that keeps fiscal records, complaints, and case documents in one '
            'organized place, making files easier to store, access, and manage.'
        ),
        'features': [
            'Central storage for fiscal records',
            'Complaints and case documents kept together',
            'Organized records that are quick to retrieve',
            'Simple interface for everyday office use',
        ],
        'stack': STACK,
    },
    {
        'slug': 'lungcheck',
        'number': '02',
        'title': 'LungCheck',
        'category': 'Machine learning · Medical imaging',
        'tagline': 'A CNN-based approach to diagnosing pneumonia, bacterial infection, and COVID-19.',
        'image': 'lungcheck.jpg',
        'image_alt': 'LungCheck pneumonia diagnosis project',
        'context': CONTEXT,
        'summary': (
            'A machine learning project that uses a Convolutional Neural Network (CNN) to '
            'classify chest X-ray images into four categories: pneumonia, bacterial, COVID-19, and normal.'
        ),
        'challenge': (
            'Reading chest X-rays accurately takes time and expertise, and several lung '
            'conditions can look alike at a glance.'
        ),
        'solution': (
            'A trained CNN model wrapped in a web app: upload a chest X-ray and get a '
            'classification across the four categories.'
        ),
        'features': [
            'Chest X-ray image upload',
            'Four-class prediction: pneumonia, bacterial, COVID-19, normal',
            'Convolutional Neural Network model',
            'Web interface built with Django',
        ],
        'stack': STACK,
    },
    {
        'slug': 'payflow',
        'number': '03',
        'title': 'PayFlow',
        'category': 'Personal finance app',
        'tagline': 'A personal budget manager and bill reminder in one place.',
        'image': 'payflow.png',
        'image_alt': 'PayFlow financial management system',
        'context': CONTEXT,
        'summary': (
            'A financial management system designed to help users monitor their finances '
            'and organize their financial records in one place.'
        ),
        'challenge': (
            'Budgets, bills, and spending records are easy to lose track of when they are '
            'spread across notes, receipts, and memory.'
        ),
        'solution': (
            'One dashboard for budgeting, bill reminders, spending categories, and a full '
            'transaction history.'
        ),
        'features': [
            'Smart budgeting to track and manage spending',
            'Bill reminders so due dates are never missed',
            'Category management to organize expenses',
            'Transaction history to review past records',
        ],
        'stack': STACK,
    },
    {
        'slug': 'serenity',
        'number': '04',
        'title': 'Serenity Tours',
        'category': 'Travel & tour booking website',
        'tagline': "Discover Biliran's islands, beaches, and highlands, then book the trip.",
        'image': 'serenity-tours.jpg',
        'image_alt': 'Serenity Tours homepage showing Sambawan Island and Maripipi, Biliran',
        'context': CONTEXT,
        'summary': (
            "A travel and tour booking website that showcases tourist spots around Biliran, "
            "from island hopping at Sambawan to its beaches and highlands."
        ),
        'challenge': (
            "Biliran has beautiful destinations, but travelers need one inviting place to "
            "discover them, compare tours, and plan a visit."
        ),
        'solution': (
            'A calm, photo-led website with tourist spot guides, services, tour pricing, '
            'and a clear "Book Now" path.'
        ),
        'features': [
            'Tourist spot showcase for Biliran',
            'Services and tour package pricing',
            'Prominent "Book Now" booking flow',
            'Contact page for trip inquiries',
        ],
        'stack': STACK,
    },
    {
        'slug': 'intelliguide',
        'number': '05',
        'title': 'IntelliGuide',
        'category': 'Assistive technology for visually impaired persons',
        'tagline': 'An assistive mobile app that helps visually impaired users move around more safely.',
        'image': 'intelliguide-camera.png',
        'image_alt': 'IntelliGuide camera screen detecting a motorcycle 2.4 m to the left and a chair 2.5 m to the right',
        # Phone screenshots: shown whole (not cropped) on a dark backdrop
        'device_shot': True,
        'gallery': [
            {
                'image': 'intelliguide-camera.png',
                'caption': 'Real-time obstacle detection',
                'alt': 'Camera screen labelling a motorcycle at 2.4 m on the left and a chair at 2.5 m on the right',
            },
            {
                'image': 'intelliguide-map.png',
                'caption': 'Navigation map with saved places',
                'alt': 'Navigation map of Naval, Biliran with saved places Home, School and balay',
            },
            {
                'image': 'intelliguide-settings.png',
                'caption': 'English, Tagalog & Bisaya voice',
                'alt': 'Settings screen with English, Tagalog and Bisaya voice language options',
            },
        ],
        'context': 'Thesis Project',
        'platform': 'Mobile App',
        'summary': (
            'IntelliGuide is an assistive mobile app that helps visually impaired users move '
            'around more safely. Using the phone’s camera, it detects obstacles in real time '
            'and tells the user what is ahead, how far it is, and which side it’s on, '
            'through both voice and vibration.'
        ),
        'challenge': (
            'Visually impaired people need to know what is in their path, how close it is, '
            'and where it is, while they are moving, without depending on an internet connection.'
        ),
        'solution': (
            'A YOLOv8 Nano model detects obstacles from the camera feed and a CNN+ViT classifier '
            'identifies them. Everything runs on the device, so the app works fully offline, '
            'and the voice feedback is available in English, Tagalog, and Bisaya.'
        ),
        'features': [
            'Real-time detection of 19 trained obstacle classes',
            'Distance estimation with a 3 m alert cutoff',
            'Left / right position of each obstacle',
            'Multimodal feedback: voice + vibration',
            'Offline barangay (location) detection',
            'Navigation map with saved places',
            'Location history kept on the phone only',
            'English, Tagalog and Bisaya support',
        ],
        'stack': ['Flutter', 'Dart', 'TensorFlow Lite', 'YOLOv8 Nano', 'CNN + ViT', 'Hive'],
        'role': 'Team Leader',
        'team': [
            {'name': 'Eliza Marie Rosario', 'role': 'Team Leader', 'is_me': True},
            {'name': 'Christine Elaine Oliverio', 'role': 'Assistant Team Leader'},
            {'name': 'Marjon Vera', 'role': 'Developer'},
            {'name': 'Carl Marco Vaporoso', 'role': 'Assistant Developer'},
        ],
    },
]
