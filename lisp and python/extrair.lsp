(defun c:extrair-strings ()
  ;; Solicita ao usuário para inserir o caminho e nome do arquivo
  (setq nome-arquivo (getstring "\nDigite o caminho completo e o nome do arquivo para salvar (exemplo: C:/meuarquivo.txt): "))

  ;; Verifica se o usuário digitou algo e se não incluiu uma extensão, adiciona ".txt"
  (if (and nome-arquivo (not (vl-string-search "." nome-arquivo))) ; Verifica se não há extensão
    (setq nome-arquivo (strcat nome-arquivo ".txt"))) ; Adiciona ".txt" caso não tenha extensão

  ;; Se o nome do arquivo não for fornecido, cria o arquivo no diretório atual do desenho
  (if (not nome-arquivo)
    (setq nome-arquivo (strcat (getvar "DWGPREFIX") "extrair-strings.txt")))

  ;; Tenta abrir o arquivo no modo "w" (gravação)
  (setq arquivo (open nome-arquivo "w"))

  ;; Verifica se o arquivo foi aberto corretamente
  (if (not arquivo)
    (progn
      (princ "\nErro ao abrir o arquivo. Verifique se você tem permissão para gravar no diretório.")
      (exit)))

  ;; Definir camadas a serem verificadas
  (setq layers '("CARIMBO_ARQUIVO" "CARIMBO_PROJETO" "CARIMBO_TITULO" 
                 "CARIMBO_DESC" "CARIMBO_ESCALA" "CARIMBO_DATA" 
                 "CARIMBO_ENDER" "CARIMBO_FASE" "CARIMBO_FOLHA" 
                 "CARIMBO_REV"))

  ;; Inicializa o contador de textos extraídos
  (setq textos-extraidos 0)

  ;; Percorre as camadas
  (foreach layer layers
    (progn
      ;; Escreve o nome da camada no arquivo
      (write-line (strcat "\n---- " layer " ----") arquivo)
      (setq ent (entnext)) ; Começa do primeiro objeto
      (while ent
        (setq ent-data (entget ent)) ; Obtém os dados do objeto
        (setq layer-name (cdr (assoc 8 ent-data))) ; Pega o nome da camada do objeto

        ;; Verifica se o objeto está na camada correta
        (if (= layer-name layer)
          (progn
            ;; Verifica se o objeto é do tipo TEXT ou MTEXT
            (if (or (= (cdr (assoc 0 ent-data)) "TEXT")  ; Verifica se o objeto é do tipo TEXT
                    (= (cdr (assoc 0 ent-data)) "MTEXT")) ; Verifica se o objeto é do tipo MTEXT
              (progn
                ;; Extrai o texto dependendo do tipo de objeto
                (setq texto (if (= (cdr (assoc 0 ent-data)) "TEXT")
                                (cdr (assoc 1 ent-data))  ; Para TEXT, a string do texto é associada à chave 1
                                (cdr (assoc 1 ent-data)))) ; Para MTEXT, a string do texto também está na chave 1
                (write-line texto arquivo) ; Escreve o texto no arquivo
                (setq textos-extraidos (1+ textos-extraidos)) ; Conta o texto extraído
              )
            )
          )
        )
        (setq ent (entnext ent)) ; Vai para o próximo objeto
      )
    ))

  ;; Fecha o arquivo após a escrita
  (close arquivo)

  ;; Exibe a mensagem de confirmação
  (if (> textos-extraidos 0)
    (princ (strcat "\nForam extraídos " (itoa textos-extraidos) " textos para o arquivo: " nome-arquivo))
    (princ "\nNenhum texto encontrado nas camadas especificadas.")
  )

  (princ)
)

(princ "\nComando 'extrair-strings' carregado. Use o comando para extrair textos das camadas especificadas.")
(princ)
