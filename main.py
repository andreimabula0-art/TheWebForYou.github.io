<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>For Jazmine</title>
    <meta
      name="description"
      content="A heartfelt thank-you website for Jazmine, celebrating her support and love."
    />
    <link rel="icon" type="image/svg+xml" href="./favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Sora:wght@300;400;500;600&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <div class="site-shell">
      <header class="hero section reveal">
        <nav class="topbar" aria-label="Primary">
          <span class="topbar__eyebrow">A grateful heart</span>
          <a class="topbar__link" href="#closing-note">Final note</a>
        </nav>
 
        <div class="hero__glow hero__glow--one" aria-hidden="true"></div>
        <div class="hero__glow hero__glow--two" aria-hidden="true"></div>
 
        <div class="hero__content">
          <p class="kicker">For Jazmine</p>
          <h1>
            Thank you for your
            <span>support, patience, and love.</span>
          </h1>
          <p class="hero__lede">
            Some people make life feel lighter just by being in it. You do that
            for me, and I wanted to make something that says thank you with the
            tenderness you deserve.
          </p>
 
          <div class="hero__actions">
            <a class="button button--solid" href="#love-notes">Read my thank you</a>
            <button class="button button--ghost" id="scrollToClosing" type="button">
              Skip to the final note
            </button>
          </div>
        </div>
 
        <aside class="hero__card reveal" aria-label="Dedication">
          <p class="hero__card-label">Dedicated to you</p>
          <p class="hero__card-copy">
            For every reassuring word, every act of care, and every moment you
            stayed close when I needed love the most.
          </p>
        </aside>
      </header>
 
      <main>
        <section class="section story reveal" aria-labelledby="story-title">
          <div class="section-heading">
            <p class="kicker">What stays with me</p>
            <h2 id="story-title">You turn ordinary moments into safe places.</h2>
          </div>
 
          <div class="story__layout">
            <p class="story__copy">
              Your love is not loud for attention. It is steady, thoughtful, and
              real. It shows up in the small things, in the way you listen, in
              the way you encourage me, and in the way you somehow make difficult
              days feel less heavy.
            </p>
            <p class="story__copy story__copy--offset">
              This page is a small reflection of something much bigger: how much
              your presence means to me. It is gratitude, admiration, and love
              wrapped together in one quiet promise that I never want to take you
              for granted.
            </p>
          </div>
        </section>
 
        <section class="section notes reveal" id="love-notes" aria-labelledby="notes-title">
          <div class="section-heading">
            <p class="kicker">The reasons are endless</p>
            <h2 id="notes-title">But here are a few I never want to forget.</h2>
          </div>
 
          <div class="notes__grid">
            <article class="note-card reveal">
              <p class="note-card__number">01</p>
              <h3>Your kindness</h3>
              <p>
                You make hard moments softer. The warmth you carry changes the
                room around you and the people in it.
              </p>
            </article>
 
            <article class="note-card note-card--featured reveal">
              <p class="note-card__number">02</p>
              <h3>Your support</h3>
              <p>
                You stand beside me with patience and grace. Your belief in me
                feels like a light I can find even on uncertain days.
              </p>
            </article>
 
            <article class="note-card reveal">
              <p class="note-card__number">03</p>
              <h3>Your love</h3>
              <p>
                Loving you feels like discovering something both beautiful and
                grounding at the same time. You make life brighter.
              </p>
            </article>
          </div>
        </section>
 
        <section class="section highlight reveal" aria-label="Signature appreciation">
          <p class="highlight__line">
            You are one of the best things that has ever happened to my heart.
          </p>
        </section>
 
        <section class="section closing reveal" id="closing-note" aria-labelledby="closing-title">
          <div class="closing__panel">
            <p class="kicker">One final thing</p>
            <h2 id="closing-title">Thank you, Jazmine.</h2>
            <p class="closing__copy">
              Thank you for your support when I need strength, for your love when
              I need warmth, and for simply being the beautiful soul that you
              are. I see your heart, I appreciate your presence, and I will
              always be grateful for you.
            </p>
            <p class="closing__signature">With all my love and gratitude.</p>
            <button class="button button--solid" id="replayButton" type="button">
              Replay the glow
            </button>
          </div>
        </section>
      </main>
 
      <footer class="footer reveal">
        <p>Made for Jazmine with love.</p>
        <p><span id="currentYear"></span> and always.</p>
      </footer>
    </div>
 
    <script src="./script.js"