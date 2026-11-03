import React from 'react';
import { createRoot } from 'react-dom/client';
import BounceCards from './components/BounceCards';

const root = document.getElementById('bounce-cards-root');
if (root) {
  const images = Array.from({ length: 9 }, (_, index) => ({
    src: root.dataset[`photo${index + 1}`],
    alt: `Elize's photo ${index + 1}`
  }));

  createRoot(root).render(
    <BounceCards
      images={images}
      className="portfolio-bounce-cards"
      containerWidth={500}
      containerHeight={400}
      cardSize={340}
      spread={25}
      rotation={10}
      arc={0}
      pushDistance={150}
      hoverScale={1.06}
      bounciness={0.6}
      animationDelay={0}
      animationStagger={0}
      borderWidth={5}
      borderColor="#fcf9f3"
      radius={25}
      shadow
      enableHover
    />
  );
}
