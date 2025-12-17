#include <iostream>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

int main() {
    std::cout << "TP-4: Client C++ avec JSON Task exact\n";
    
    try {
        std::cout << "\n=== 1. GET Task ===" << std::endl;
        auto get_resp = cpr::Get(cpr::Url{"http://localhost:8000/"});
        
        if (get_resp.status_code != 200) {
            std::cout << "Erreur GET: " << get_resp.status_code << " - " << get_resp.text << std::endl;
            return 1;
        }
        
        std::cout << "Réponse GET (" << get_resp.text.size() << " chars)" << std::endl;
        
        auto task_json = json::parse(get_resp.text);
        
        if (!task_json.contains("size") || !task_json.contains("A") || 
            !task_json.contains("B") || !task_json.contains("x")) {
            std::cout << "JSON invalide: champs manquants" << std::endl;
            std::cout << "Champs présents: ";
            for (auto& el : task_json.items()) {
                std::cout << el.key() << " ";
            }
            std::cout << std::endl;
            return 1;
        }
        
        std::cout << "Task valide: size=" << task_json["size"] 
                  << ", A: " << task_json["A"].size() << "x" 
                  << (task_json["A"].size() > 0 ? task_json["A"][0].size() : 0)
                  << ", x is null: " << task_json["x"].is_null() << std::endl;
        
        std::cout << "\n=== 2. POST Task ===" << std::endl;
        
        auto post_resp = cpr::Post(
            cpr::Url{"http://localhost:8000/"},
            cpr::Header{{"Content-Type", "application/json"}},
            cpr::Body{task_json.dump()}
        );
        
        std::cout << "POST réponse: " << post_resp.text << std::endl;
        std::cout << "Code HTTP: " << post_resp.status_code << std::endl;
        
        if (post_resp.status_code == 200) {
            std::cout << "\n SUCCÈS: Communication C++ ↔ Python fonctionne!" << std::endl;
        }
        
    } catch (const json::parse_error& e) {
        std::cout << "Erreur JSON: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Erreur: " << e.what() << std::endl;
    }
    
    return 0;
}
