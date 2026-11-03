import React from 'react';
import { createRoot } from 'react-dom/client';
import Lanyard from './components/Lanyard';

const root = document.getElementById('lanyard-root');
if (root) {
  createRoot(root).render(
    <Lanyard
      frontImage={root.dataset.frontImage}
      backImage={root.dataset.backImage}
      strapImage={root.dataset.strapImage}
      imageFit="cover"
      cardColor="#4b382c"
      orientation="portrait"
      finish="glossy"
      cornerRadius={0.3}
      size={0.6}
      anchor="right"
      strapLength={0.5}
      strapColor="#111111"
      strapWidth={0.65}
      metal="silver"
      gravity={1}
      damping={0.5}
      elasticity={0.5}
      breeze={0}
      introDelay={0}
      interactive
      intro
      style={{ width: '100%', height: '100%' }}
    />
  );
}
