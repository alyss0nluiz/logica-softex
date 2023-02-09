import './App.css';
import Dados from './components/Dados';


function App() {

  const nome='Alysson Luiz'
  const idade='20 years'
  const cargo='Coordenador de Redes e Multiserviços'
  
  return (
  <>
    <Dados nome={nome} idade={idade} cargo={cargo} />
  </>
  )
}

export default App;
