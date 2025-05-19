export function formatNumberShort(num) {
    const absNum = Math.abs(num);

    const format = (value, suffix) => {
        return value % 1 === 0
        ? `${value}${suffix}`
        : `${value.toFixed(2).replace('.', '.')}${suffix}`;
    };

    if (absNum < 1_000) {
        return num.toString(); // Без сокращения
    } else if (absNum < 1_000_000) {
        return format(num / 1_000, 'k');
    } else if (absNum < 1_000_000_000) {
        return format(num / 1_000_000, 'M');
    } else if (absNum < 1_000_000_000_000) {
        return format(num / 1_000_000_000, 'B');
    } else {
        return format(num / 1_000_000_000_000, 'BB');
    }
}

export function getLevelByCards(cardCount, levelsConfig) {
    const levels = Object.keys(levelsConfig)
      .map(Number)
      .sort((a, b) => a - b);
  
    let total = 0;
  
    for (let i = 0; i < levels.length; i++) {
      const lvl = levels[i];
      const nextLvl = levels[i + 1];
      const cardsRequired = Number(levelsConfig[lvl].cardsCountUpLevel);
      total += cardsRequired;
  
      if (!nextLvl || cardCount < total) {
        return lvl;
      }
    }
  
    return levels[levels.length - 1];
  }
  

export function getLevelByTotalPoints(points, levelsConfig) {
    const levels = Object.keys(levelsConfig)
      .map(Number)
      .sort((a, b) => a - b);
  
    let previousThreshold = 0;
  
    for (const lvl of levels) {
      const currentThreshold = Number(levelsConfig[lvl].pointsUpLevel);
  
      if (points < currentThreshold) {
        return lvl;
      }
  
      previousThreshold = currentThreshold;
    }
  
    return levels[levels.length - 1];
}

export function getRouteName(){
  const route = useRoute()
  switch(route.fullPath){
      case '/':
          return 'Store'
      case '/liderbord':
          return 'Liderbord'
      case '/profile':
          return 'Profile'
      case '/friends':
          return 'Friends'
      case '/tasks':
          return 'Tasks'
  }

}  
  