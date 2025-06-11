// src/components/EquipmentCard.tsx

import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { AlertTriangle, CheckCircle, AlertCircle, BrainCircuit } from 'lucide-react';

interface EquipmentCardProps {
  equipment: any; // Usado 'any' para incluir a nova propriedade 'prediction'
  alerts: any[];
}

const EquipmentCard: React.FC<EquipmentCardProps> = ({ equipment, alerts }) => {
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'normal': return 'text-green-400';
      case 'warning': return 'text-yellow-400';
      case 'critical': return 'text-red-400';
      default: return 'text-gray-400';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'normal': return <CheckCircle className="w-5 h-5" />;
      case 'warning': return <AlertCircle className="w-5 h-5" />;
      case 'critical': return <AlertTriangle className="w-5 h-5" />;
      default: return <CheckCircle className="w-5 h-5" />;
    }
  };
  
  const criticalAlerts = alerts.filter(alert => alert.severity === 'critical').length;
  const warningAlerts = alerts.filter(alert => alert.severity === 'warning').length;

  return (
    <Card className="bg-slate-800 border-slate-700 hover:bg-slate-750 transition-colors flex flex-col justify-between">
      <div>
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle className="text-lg text-white">{equipment.name}</CardTitle>
            <div className={`flex items-center gap-2 ${getStatusColor(equipment.status)}`}>
              {getStatusIcon(equipment.status)}
              <span className="capitalize font-medium">{equipment.status}</span>
            </div>
          </div>
          <p className="text-slate-400 text-sm">{equipment.location}</p>
        </CardHeader>
        
        <CardContent className="space-y-4">
          {/* Alertas */}
          {(criticalAlerts > 0 || warningAlerts > 0) && (
            <div className="flex gap-2">
              {criticalAlerts > 0 && (
                <Badge variant="destructive" className="bg-red-500/20 text-red-400 border-red-500">
                  {criticalAlerts} Crítico(s)
                </Badge>
              )}
              {warningAlerts > 0 && (
                <Badge variant="secondary" className="bg-yellow-500/20 text-yellow-400 border-yellow-500">
                  {warningAlerts} Aviso(s)
                </Badge>
              )}
            </div>
          )}

          {/* Sensores */}
          <div className="space-y-3">
            {/* Temperatura */}
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-sm text-slate-300">Temperatura</span>
                <span className="text-sm font-medium text-white">
                  {equipment.sensors.temperature}°C
                </span>
              </div>
              <Progress 
                value={(equipment.sensors.temperature / 100) * 100} 
                className="h-2 bg-slate-700"
              />
            </div>

            {/* Vibração */}
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-sm text-slate-300">Vibração</span>
                <span className="text-sm font-medium text-white">
                  {equipment.sensors.vibration} Hz
                </span>
              </div>
              <Progress 
                value={(equipment.sensors.vibration / 50) * 100} 
                className="h-2 bg-slate-700"
              />
            </div>

            {/* RPM */}
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-sm text-slate-300">Rotação</span>
                <span className="text-sm font-medium text-white">
                  {equipment.sensors.rpm} RPM
                </span>
              </div>
              <Progress 
                value={(equipment.sensors.rpm / 3000) * 100} 
                className="h-2 bg-slate-700"
              />
            </div>
          </div>
        </CardContent>
      </div>

      {/* --- Seção de Previsão Preditiva --- */}
      <CardContent className="mt-auto">
        {equipment.prediction ? (
          <div className={`p-3 rounded-lg ${equipment.prediction.falha_prevista ? 'bg-red-500/10' : 'bg-green-500/10'}`}>
            <div className="flex items-center gap-2 mb-2">
              <BrainCircuit className="w-5 h-5" />
              <h4 className="font-semibold text-white">Previsão Preditiva</h4>
            </div>
            {equipment.prediction.falha_prevista ? (
              <div>
                <Badge variant="destructive">Risco de Falha Iminente</Badge>
                <p className="text-sm text-slate-300 mt-1">
                  Probabilidade de falha: <span className="font-bold">{(equipment.prediction.probabilidade_falha * 100).toFixed(1)}%</span>
                </p>
              </div>
            ) : (
              <div>
                <Badge variant="default" className="bg-green-600">Operação Normal</Badge>
                 <p className="text-sm text-slate-300 mt-1">
                  Probabilidade de falha: <span className="font-bold">{(equipment.prediction.probabilidade_falha * 100).toFixed(1)}%</span>
                </p>
              </div>
            )}
          </div>
        ) : (
          <div className="p-3 rounded-lg bg-slate-700/50 text-center">
            <p className="text-sm text-slate-400">Aguardando predição...</p>
          </div>
        )}
        <div className="text-xs text-slate-400 pt-2 border-t border-slate-700 mt-4">
          Última atualização: {new Date(equipment.lastReading).toLocaleTimeString('pt-BR')}
        </div>
      </CardContent>
    </Card>
  );
};

export default EquipmentCard;