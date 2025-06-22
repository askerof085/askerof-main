// quiz.js

// Utility: Shuffle array (Fisher-Yates)
function shuffle(array) {
  let currentIndex = array.length, randomIndex;
  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
  }
  return array;
}

// State
let quizQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let correctCount = 0;
let userAnswers = [];
let difficultyStats = { Easy: { total: 0, correct: 0 }, Medium: { total: 0, correct: 0 }, Hard: { total: 0, correct: 0 } };
let totalQuestions = 10;

// DOM Elements
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultsScreen = document.getElementById('results-screen');
const reviewScreen = document.getElementById('review-screen');
const startBtn = document.getElementById('start-btn');
const nextBtn = document.getElementById('next-btn');
const retryBtn = document.getElementById('retry-btn');
const reviewBtn = document.getElementById('review-btn');
const prevReviewBtn = document.getElementById('prev-review-btn');
const nextReviewBtn = document.getElementById('next-review-btn');
const backToResultsBtn = document.getElementById('back-to-results-btn');
const questionCountSelect = document.getElementById('question-count');
const questionCounter = document.getElementById('question-counter');
const scoreDisplay = document.getElementById('score-display');
const questionText = document.getElementById('question-text');
const optionA = document.getElementById('option-a');
const optionB = document.getElementById('option-b');
const optionC = document.getElementById('option-c');
const optionD = document.getElementById('option-d');
const optionsContainer = document.querySelector('.options-container');
const difficultyBadge = document.getElementById('difficulty-badge');
const topicTag = document.getElementById('topic-tag');
const finalScore = document.getElementById('final-score');
const correctCountDisplay = document.getElementById('correct-count');
const totalQuestionsDisplay = document.getElementById('total-questions');
const difficultyStatsDiv = document.getElementById('difficulty-stats');
const customQuestionCount = document.getElementById('custom-question-count');
const totalAvailableSpan = document.getElementById('total-available');

// Review elements
const reviewQuestionText = document.getElementById('review-question-text');
const reviewOptionA = document.getElementById('review-option-a');
const reviewOptionB = document.getElementById('review-option-b');
const reviewOptionC = document.getElementById('review-option-c');
const reviewOptionD = document.getElementById('review-option-d');
const reviewOptionsContainer = document.querySelector('.review-options');
const reviewDifficultyBadge = document.getElementById('review-difficulty-badge');
const reviewTopicTag = document.getElementById('review-topic-tag');
const reviewCounter = document.getElementById('review-counter');
const explanationText = document.getElementById('explanation-text');

// Review state
let currentReviewIndex = 0;

// Update total available questions count
totalAvailableSpan.textContent = questions.length;
customQuestionCount.max = questions.length;

// Start Quiz
questionCountSelect.addEventListener('change', () => {
  if (questionCountSelect.value === 'custom') {
    customQuestionCount.style.display = 'block';
    customQuestionCount.focus();
  } else {
    customQuestionCount.style.display = 'none';
  }
});

startBtn.addEventListener('click', () => {
  if (questionCountSelect.value === 'custom') {
    const customVal = parseInt(customQuestionCount.value, 10);
    if (!isNaN(customVal) && customVal > 0 && customVal <= questions.length) {
      totalQuestions = customVal;
    } else {
      alert(`Please enter a valid number between 1 and ${questions.length}`);
      return;
    }
  } else if (questionCountSelect.value === 'all') {
    totalQuestions = questions.length;
  } else {
    totalQuestions = parseInt(questionCountSelect.value, 10);
  }
  startQuiz();
});

function startQuiz() {
  // Reset state
  score = 0;
  correctCount = 0;
  userAnswers = [];
  difficultyStats = { Easy: { total: 0, correct: 0 }, Medium: { total: 0, correct: 0 }, Hard: { total: 0, correct: 0 } };
  currentQuestionIndex = 0;
  // Randomly select questions
  quizQuestions = shuffle([...questions]).slice(0, totalQuestions);
  // UI
  startScreen.classList.remove('active');
  resultsScreen.classList.remove('active');
  quizScreen.classList.add('active');
  updateScoreDisplay();
  showQuestion();
}

function showQuestion() {
  const q = quizQuestions[currentQuestionIndex];
  questionText.textContent = q.text;
  optionA.textContent = q.options.a;
  optionB.textContent = q.options.b;
  optionC.textContent = q.options.c;
  optionD.textContent = q.options.d;
  difficultyBadge.textContent = q.difficulty;
  difficultyBadge.className = `difficulty-badge ${q.difficulty.toLowerCase()}`;
  topicTag.textContent = q.topic;
  // Reset option states
  Array.from(optionsContainer.children).forEach(opt => {
    opt.classList.remove('selected', 'correct', 'incorrect');
    opt.style.pointerEvents = 'auto';
  });
  nextBtn.disabled = true;
  // Update counter
  questionCounter.textContent = `Question ${currentQuestionIndex + 1} of ${totalQuestions}`;
}

optionsContainer.addEventListener('click', (e) => {
  const optionDiv = e.target.closest('.option');
  if (!optionDiv) return;
  if (nextBtn.disabled === false) return; // Already answered
  // Mark selected
  Array.from(optionsContainer.children).forEach(opt => opt.classList.remove('selected'));
  optionDiv.classList.add('selected');
  // Check answer
  const selected = optionDiv.getAttribute('data-option');
  const q = quizQuestions[currentQuestionIndex];
  const isCorrect = selected === q.answer;
  if (isCorrect) {
    optionDiv.classList.add('correct');
    correctCount++;
    difficultyStats[q.difficulty].correct++;
  } else {
    optionDiv.classList.add('incorrect');
    // Highlight correct
    Array.from(optionsContainer.children).forEach(opt => {
      if (opt.getAttribute('data-option') === q.answer) {
        opt.classList.add('correct');
      }
    });
  }
  difficultyStats[q.difficulty].total++;
  userAnswers.push({
    question: q.text,
    selected,
    correct: q.answer,
    options: q.options,
    difficulty: q.difficulty,
    topic: q.topic
  });
  // Disable further selection
  Array.from(optionsContainer.children).forEach(opt => {
    opt.style.pointerEvents = 'none';
  });
  nextBtn.disabled = false;
  updateScoreDisplay();
});

nextBtn.addEventListener('click', () => {
  currentQuestionIndex++;
  if (currentQuestionIndex < quizQuestions.length) {
    showQuestion();
  } else {
    showResults();
  }
});

function updateScoreDisplay() {
  // Calculate score as percentage
  score = Math.round((correctCount / totalQuestions) * 100);
  scoreDisplay.textContent = `Score: ${score}%`;
}

function showResults() {
  quizScreen.classList.remove('active');
  resultsScreen.classList.add('active');
  // Calculate final score as percentage
  const finalScoreValue = Math.round((correctCount / totalQuestions) * 100);
  finalScore.textContent = finalScoreValue;
  correctCountDisplay.textContent = correctCount;
  totalQuestionsDisplay.textContent = totalQuestions;
  // Difficulty breakdown
  difficultyStatsDiv.innerHTML = '';
  Object.keys(difficultyStats).forEach(level => {
    const stat = difficultyStats[level];
    if (stat.total > 0) {
      const percent = Math.round((stat.correct / stat.total) * 100);
      difficultyStatsDiv.innerHTML += `<div class="difficulty-stat"><span>${level}</span><span>${stat.correct} / ${stat.total} (${percent}%)</span></div>`;
    }
  });
}

retryBtn.addEventListener('click', () => {
  startScreen.classList.add('active');
  resultsScreen.classList.remove('active');
});

reviewBtn.addEventListener('click', () => {
  currentReviewIndex = 0;
  showReview();
});

prevReviewBtn.addEventListener('click', () => {
  if (currentReviewIndex > 0) {
    currentReviewIndex--;
    showReview();
  }
});

nextReviewBtn.addEventListener('click', () => {
  if (currentReviewIndex < userAnswers.length - 1) {
    currentReviewIndex++;
    showReview();
  }
});

backToResultsBtn.addEventListener('click', () => {
  reviewScreen.classList.remove('active');
  resultsScreen.classList.add('active');
});

function showReview() {
  resultsScreen.classList.remove('active');
  reviewScreen.classList.add('active');
  
  const answer = userAnswers[currentReviewIndex];
  const q = quizQuestions[currentReviewIndex];
  
  // Update question info
  reviewQuestionText.textContent = answer.question;
  reviewDifficultyBadge.textContent = q.difficulty;
  reviewDifficultyBadge.className = `difficulty-badge ${q.difficulty.toLowerCase()}`;
  reviewTopicTag.textContent = q.topic;
  
  // Update options
  reviewOptionA.textContent = q.options.a;
  reviewOptionB.textContent = q.options.b;
  reviewOptionC.textContent = q.options.c;
  reviewOptionD.textContent = q.options.d;
  
  // Reset option states
  Array.from(reviewOptionsContainer.children).forEach(opt => {
    opt.classList.remove('correct', 'incorrect', 'user-selected');
  });
  
  // Mark correct answer
  Array.from(reviewOptionsContainer.children).forEach(opt => {
    if (opt.getAttribute('data-option') === answer.correct) {
      opt.classList.add('correct');
    }
    if (opt.getAttribute('data-option') === answer.selected) {
      opt.classList.add('user-selected');
      if (answer.selected !== answer.correct) {
        opt.classList.add('incorrect');
      }
    }
  });
  
  // Update explanation
  explanationText.textContent = q.explanation || 'No explanation available for this question.';
  
  // Update counter
  reviewCounter.textContent = `Question ${currentReviewIndex + 1} of ${userAnswers.length}`;
  
  // Update navigation buttons
  prevReviewBtn.disabled = currentReviewIndex === 0;
  nextReviewBtn.disabled = currentReviewIndex === userAnswers.length - 1;
} 